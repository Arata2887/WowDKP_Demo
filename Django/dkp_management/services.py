from .models import Player, DKPLog

def add_dkp(players, points: int, note: str):
    """
    给多个玩家增加DKP分数，并记录操作日志，同时更新玩家的总分。
    
    参数:
    players -- 单个 Player 实例或 Player 实例的列表
    points -- 增加的分数
    note -- 备注信息，必须提供加分理由
    """
    if not isinstance(players, list):
        players = [players]  # 如果传入的是单个玩家，将其转换为列表

    dkp_logs = []
    for player in players:
        # 更新玩家总分
        player.total_dkp += points
        player.save()

        # 创建加分日志
        dkp_logs.append(DKPLog(player=player, points=points, action_type='add', note=note))

    # 批量创建DKP日志
    DKPLog.objects.bulk_create(dkp_logs)


def remove_dkp(players, points: int, note: str):
    """
    从多个玩家的DKP分数中扣除，并记录操作日志，同时更新玩家的总分。
    
    参数:
    players -- 单个 Player 实例或 Player 实例的列表
    points -- 扣除的分数
    note -- 备注信息，必须提供扣分理由
    """
    if not isinstance(players, list):
        players = [players]

    dkp_logs = []
    for player in players:
        # 更新玩家总分
        player.total_dkp -= points
        player.save()

        # 创建扣分日志
        dkp_logs.append(DKPLog(player=player, points=points, action_type='remove', note=note))

    # 批量创建DKP日志
    DKPLog.objects.bulk_create(dkp_logs)


def calculate_total_dkp(player: Player) -> int:
    """
    获取玩家的当前总DKP分数，直接从 total_dkp 字段中返回。
    """
    return player.total_dkp
