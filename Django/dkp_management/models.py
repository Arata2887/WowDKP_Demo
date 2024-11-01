from django.db import models
from django.core.exceptions import ValidationError

class Player(models.Model):
    # 角色名
    character_name = models.CharField(max_length=100, unique=True)
    # 职业，例如“战士”，“法师”
    profession = models.CharField(max_length=50)
    # 职责，例如“坦克”，“治疗”
    role = models.CharField(max_length=50)
    # 专精，例如“防护”，“火焰”
    specialization = models.CharField(max_length=50)
    
    def __str__(self):
        return self.character_name


class DKPLog(models.Model):
    ACTION_CHOICES = [
        ('add', '增加'),
        ('remove', '减少'),
    ]
    player = models.ForeignKey(Player, on_delete=models.CASCADE)  # 关联的玩家
    points = models.IntegerField()  # 加减的分数
    action_type = models.CharField(max_length=10, choices=ACTION_CHOICES)  # 操作类型
    timestamp = models.DateTimeField(auto_now_add=True)  # 操作时间
    note = models.TextField(blank=True, null=True)  # 备注（可选）

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
