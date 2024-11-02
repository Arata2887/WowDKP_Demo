import pandas as pd

# 定义职业和职责的选项
profession_options = [
    '死亡骑士', '恶魔猎手', '德鲁伊', '唤魔师', '猎人', 
    '法师', '武僧', '圣骑士', '牧师', '潜行者', 
    '萨满', '术士', '战士'
]

role_options = ['坦克', '治疗', '输出']

# 创建 DataFrame 模板，增加"角色名"列，职业和职责下拉列
data = {
    '角色名': [''] * len(profession_options),   # 空白供用户填写
    '职业': profession_options,
    '职责': [''] * len(profession_options)      # 初始为空
}

template_df = pd.DataFrame(data)

# 保存到 Excel 文件
file_path_custom = 'Player_Import_Template_Custom.xlsx'
with pd.ExcelWriter(file_path_custom, engine='xlsxwriter') as writer:
    template_df.to_excel(writer, index=False, sheet_name='角色信息模板')

    workbook  = writer.book
    worksheet = writer.sheets['角色信息模板']

    # 设置"职业"列为下拉菜单
    worksheet.data_validation('B2:B100', {
        'validate': 'list',
        'source': profession_options
    })

    # 设置"职责"列为下拉菜单
    worksheet.data_validation('C2:C100', {
        'validate': 'list',
        'source': role_options
    })

file_path_custom

