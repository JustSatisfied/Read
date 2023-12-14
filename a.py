import itchat

# 登录微信
itchat.auto_login()

# 获取好友列表
friends = itchat.get_friends()

# 遍历好友列表，找到需要发送消息的好友
for friend in friends:
    # 指定好友的备注名或昵称
    if friend['RemarkName'] == '吗喽':
        # 发送消息
        itchat.send('你好，这是一条自动发送的消息。', toUserName=friend['UserName'])
        break