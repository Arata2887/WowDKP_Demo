from django.db import models
from django.core.exceptions import ValidationError

class Player(models.Model):
    # 职业选项
    PROFESSION_CHOICES = [
        ('Death Knight', '死亡骑士'),
        ('Demon Hunter', '恶魔猎手'),
        ('Druid', '德鲁伊'),
        ('Evoker', '唤魔师'),
        ('Hunter', '猎人'), 
        ('Mage', '法师'), 
        ('Monk', '武僧'), 
        ('Paladin', '圣骑士'),
        ('Priest', '牧师'), 
        ('Rogue', '潜行者'), 
        ('Shaman', '萨满'), 
        ('Warlock', '术士'), 
        ('Warrior', '战士')
    ]

    # 职责选项
    ROLE_CHOICES = [
        ('Tank', '坦克'),
        ('Healer', '治疗'),
        ('DPS', '输出')
    ]

    # 专精选项，按职业分类
    SPECIALIZATION_CHOICES = {
        'Death Knight': [('Blood', '血魄'), ('Frost', '冰霜'), ('Unholy', '邪恶')],
        'Demon Hunter': [('Havoc', '浩劫'), ('Vengeance', '复仇')],
        'Druid': [('Balance', '平衡'), ('Feral', '野性'), ('Guardian', '守护'), ('Restoration', '恢复')],
        'Evoker': [('Devastation', '毁灭'), ('Preservation', '保存')],
        'Hunter': [('Beast Mastery', '野兽控制'), ('Marksmanship', '射击'), ('Survival', '生存')],
        'Mage': [('Arcane', '奥术'), ('Fire', '火焰'), ('Frost', '冰霜')],
        'Monk': [('Brewmaster', '酒仙'), ('Mistweaver', '织雾'), ('Windwalker', '踏风')],
        'Paladin': [('Holy', '神圣'), ('Protection', '防护'), ('Retribution', '惩戒')],
        'Priest': [('Discipline', '戒律'), ('Holy', '神圣'), ('Shadow', '暗影')],
        'Rogue': [('Assassination', '奇袭'), ('Outlaw', '狂徒'), ('Subtlety', '敏锐')],
        'Shaman': [('Elemental', '元素'), ('Enhancement', '增强'), ('Restoration', '恢复')],
        'Warlock': [('Affliction', '痛苦'), ('Demonology', '恶魔学识'), ('Destruction', '毁灭')],
        'Warrior': [('Arms', '武器'), ('Fury', '狂怒'), ('Protection', '防护')]
    }

    # 角色名
    character_name = models.CharField(max_length=100, unique=True)
    # 职业，例如“战士”，“法师”
    profession = models.CharField(max_length=50, choices=PROFESSION_CHOICES)
    # 职责，例如“坦克”，“治疗”
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    # 专精，例如“防护”，“火焰”（可为空）
    specialization = models.CharField(max_length=50, blank=True, null=True)
    # DKP总分
    total_dkp = models.IntegerField(default=0) 

    def save(self, *args, **kwargs):
        # 如果 specialization 不为空，确保专精符合选择的职业
        if self.specialization:
            valid_specializations = dict(self.SPECIALIZATION_CHOICES).get(self.profession, [])
            if self.specialization not in [spec[0] for spec in valid_specializations]:
                raise ValueError(f"{self.specialization} 不是合法的专精选项。")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.character_name


class Raid(models.Model):
    # 副本名称，例如“尼鲁巴尔王宫”
    name = models.CharField(max_length=100)
    # 副本版本，例如“11.0” 或 “怀旧服”
    version = models.CharField(max_length=50, blank=True, null=True)
    # 副本描述（可选）
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (版本: {self.version})" if self.version else self.name


class Boss(models.Model):
    # BOSS 编号，例如 "H8", "M4"（在同一副本内唯一）
    boss_id = models.CharField(max_length=10)  # 无需全局唯一

    # BOSS 名称，例如“奈法利安”
    name = models.CharField(max_length=100)
    
    # 所属副本
    raid = models.ForeignKey(Raid, on_delete=models.CASCADE, related_name='bosses')
    
    # BOSS 描述（可选）
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.raid.name} - {self.boss_id} - {self.name}"

    class Meta:
        # 设置联合唯一约束，使 boss_id 在每个 Raid 内唯一
        unique_together = ('raid', 'boss_id')



class DKPLog(models.Model):
    ACTION_CHOICES = [
        ('add', '增加'),
        ('remove', '减少'),
    ]
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    points = models.IntegerField()  # 加减的分数
    action_type = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField()  # 备注信息

    # 关联的副本和BOSS
    raid = models.ForeignKey(Raid, on_delete=models.CASCADE, null=True, blank=True)
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.player.character_name} - {self.action_type} {self.points}"


class EquipmentType(models.Model):
    EQUIPMENT_CATEGORY_CHOICES = [
        ('武器', '武器'),
        ('护甲', '护甲'),
        ('戒指', '戒指'),
        ('项链', '项链'),
        ('饰品', '饰品'),
        ('特殊物品', '特殊物品'),  # 包括坐骑、食谱等
    ]
    
    # 装备分类
    category = models.CharField(max_length=20, choices=EQUIPMENT_CATEGORY_CHOICES)
    
    # 特殊词缀
    is_rare_drop = models.BooleanField(default=False)  # 是否为稀有掉落
    is_set_item = models.BooleanField(default=False)   # 是否为套装物品

    def clean(self):
        # 约束：套装物品必须是护甲类型，且不能为稀有掉落
        if self.is_set_item:
            if self.category != '护甲':
                raise ValidationError("套装物品必须为护甲类型。")
            if self.is_rare_drop:
                raise ValidationError("套装物品不能为稀有掉落。")
    
    def __str__(self):
        special_tags = []
        if self.is_rare_drop:
            special_tags.append("稀有掉落")
        if self.is_set_item:
            special_tags.append("套装物品")
        return f"{self.category} ({', '.join(special_tags)})" if special_tags else self.category

class EventRule(models.Model):
    # 事件名称，例如“击杀boss（farm）”、“犯错惩罚”
    name = models.CharField(max_length=100, unique=True)
    # 分数值（正数为加分，负数为扣分）
    points = models.IntegerField()

    def __str__(self):
        return f"{self.name}: {self.points} DKP"