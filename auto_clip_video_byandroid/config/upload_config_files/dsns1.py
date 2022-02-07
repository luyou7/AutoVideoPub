''' 《国剧：屌丝男士 第一季》 设定上传视频的配置参数 '''
module_instruction = '《国剧：屌丝男士 第一季》 设定上传视频的配置参数'

# 手机连接电脑后，存储区的盘符
# TODO: 注意目前这个是有问题的，还不知道电脑怎么访问到 手机存储空间，现在这样写认为是当前工程根目录下的
mobile_drive_path = 'EPCNSZUW1067\\nova 8\\内部存储'
# 手机存储区根目录下的用于存放自动脚本所需视频文件的文件夹
# 一定要确保手机文件管理的根目录下有这个文件夹
# 自动脚本里自动组合的视频一定要放到这个文件夹下（有些手机，不能在电脑磁盘里直接访问，需要靠手机助手，
# 这种情况就只能先执行视频组合脚本，然后手动把生成的视频文件复制到手机里的这个文件夹下）
mobile_storage_folder = 'autopy_for_bijian'

# 分解视频或合并视频 的 文件类型(.ts .mp4 等)
video_file_Format = ".mp4"

# 爬视频的脚本配置文件的所在目录（文件夹名称）
video_py_file_root_dir = 'video_vars_dandanzan'
# 已爬取到的视频文件的所在目录（文件夹名称）
video_download_file_root_dir = 'downloadvideo'
# 每个输出片段的最短时长（单位：分钟）（如果实际生成视频时，计算出的实际分段视频时长小于该值，则不会进行输出视频文件）
paragraph_min_long_m = 1

# 要上传哪几集
# 拆解成数组方式：'01,02'.split(',') 
# 目前支持两种写法：[1] '01,02,03,04,05'; [2] '1:5' 这表示范围 等同于第一种的效果
upload_video_episode_list = '01'
first_name = 'dsns'
second_name = 'dsns1'
# 对相应视频进行处理的配置参数
# （注：每个 .ts 视频文件的时长大约 3秒）
video_file_config_list = [
  {
    # 下的 一级目录(文件夹名)
    'first_name': first_name,
    # 下的 二级目录脚本文件(.py 脚本文件名) [即上面一个目录下的具体文件]
    'second_name': second_name, # 表示 第 N 季
    # 要上传哪几集
    # 拆解成数组方式：'01,02'.split(',') 
    # 目前支持两种写法：[1] '01,02,03,04,05'; [2] '1:5' 这表示范围 等同于第一种的效果
    "episode_list": upload_video_episode_list,
    # [*] 某一季下的 一集视频的 剪辑参数（每一集的剪辑参数都是统一的）
    # 剪辑组合的 开始时刻（一定要按照下面的格式，否则报错）
    'start_percent': '00:01:37',
    # 剪辑组合的 结束时刻（一定要按照下面的格式，否则报错）
    'end_percent': '00:10:55',
    # 一个 .ts 视频文件的时长（单位：秒）(属性名最后的 s 代表单位是 秒)
    'ts_unit_long_s': 3,
    # 剪辑成 N 段【这只能控制最多的输出分段数，如果实际视频总量不足，则实际会少于该数量】
    'paragraph': 3,
    # 每一段的时长（单位：分钟）(属性名最后的 m 代表单位是 分钟)
    # 【注：这只能是个大约的时间，最终生成的会有偏差】
    'paragraph_long_m': 2,
    # 每一段剪辑视频的 间隔时长（单位：秒）
    'paragraph_span': 5
  }
]

# 视频上传的配置参数
# 作用：
# 1、会根据这里的配置参数，把工程中已经输出的视频文件 复制到 手机存储区中
# 2、会根据这里的配置参数，然后自动<必剪 app>上传脚本会直接读取已复制过去视频的整个文件夹内容，进行自动上传视频操作
video_upload_config_list = [
  {
    # 下的 一级目录(文件夹名)
    'first_name': first_name,
    # 下的 二级目录脚本文件(.py 脚本文件名) [即上面一个目录下的具体文件]
    'second_name': second_name, # 表示 第 N 季
    # 要上传哪几集
    # 拆解成数组方式：'01,02'.split(',') 
    "episode_list": upload_video_episode_list,
    # 要上传的视频分段的序号（视频分段文件的完整名称例如 silliconvalley1_01.mp4 只要知道分段序号就能拼接出完整的视频文件路径）
    # 拆解成数组方式：'03,04'.split(',') 
    # 目前支持两种写法：[1] '01,02,03,04,05'; [2] '1:5' 这表示范围 等同于第一种的效果
    # 'paragraph_serials':'01,02,03,04,05',
    'paragraph_serials':'1:3',
    # ------ <必剪 app> 导出画面里要填写的相关参数 start -----------
    # 分区
    'upload_channel': '生活,搞笑',
    # 标题（这个标题决定固定的前缀，实际标题后面会动态追加当前上传的视频 第几集 第几段 的参数）
    'upload_title': '-《国剧：屌丝男士》片段--第{0}季，第{1}集--{2}; 2022一起笑一笑',
    # 类型
    'upload_type': '自制',
    # 标签
    'upload_tags': '生活,搞笑,屌丝,休闲,娱乐,国剧',
    # 标签--参与话题（请只设置一项即可）（注：经测试话题参与只能选一项，虽然我程序里支持多项，但是就设置了多项，<必剪 app>也会把后一项覆盖前一项）
    # 'upload_tags_subject': '2022年新年锦鲤,2022第一次打卡',
    'upload_tags_subject': '虚拟UP主召集令',
    # 简介
    'instroduction': '《国剧：屌丝男士》片段，休闲娱乐，恰饭必备',
    # 动态
    'upload_dynamic': '《国剧：屌丝男士》片段',
    # 封面修改功能（支持的封面功能请查看 /auto_clip_video_byandroid/edit_pubcover_action/ 下的功能脚本）
    # 封面类型页签
    'cover_type': '搞笑2',
    # 封面类型页签下的 具体封面选项（行号，列号）
    'cover_item': (1,3),
    # 封面中文本的内容，不同的封面选项有不同数量的文本，需要使用者自己清楚要修改哪些文本，如果为空的，则不会修改原来的文本
    # 填入规则是：从上到下 > 从左到右 依次把 cover_text_list 列表中的内容进行填入（cover_text_list 中若内容数量缺少则不修改，若有多余的则不管）
    'cover_text_list': [
      '百看不腻'
    ]
    # ------ <必剪 app> 导出画面里要填写的相关参数 end -----------
  }
]