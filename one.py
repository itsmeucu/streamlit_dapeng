# https://blog.csdn.net/weixin_43894266/article/details/115833698

# import numpy as np


# with st.file_input() as input:
#   if input == None:
#     st.warning('No file selected.')
#   else:
#     file_contents = input.read()

# conn = sqlite3.connect('dapeng.db')


# 返回用户选择的学院id,第一层,collage_id
def collage_infos_id():
    st.markdown('''## 学院名称''')
    st.text('''# 点击不会有任何操作''')
    cur = conn.execute("select collage_id,collage_name from Type_Of_Lessons group by collage_name;").fetchall()
    cols_info_c = st.columns(len(cur))  # 显示学院的按钮用
    list_collage_name = []
    for index, button_name in enumerate(cur):
        cols_info_c[index].button(button_name[1], args=(button_name[1]),
                                  # on_click=print('b'),
                                  help=str(button_name), )
        list_collage_name.append(button_name[1])
    opt_collage_name = ['请选择一个学院']
    for aa in list_collage_name:
        opt_collage_name.append(aa)
    # opt_collage_name = list_collage_name.index(str())
    option_collage_name = st.selectbox('', opt_collage_name)
    # collage_id = []
    if option_collage_name == '请选择一个学院':
        st.text('您尚未选择任何学院，请选择一个学院')
        return []
    else:
        # st.text(option_collage_name)
        for cu in cur:
            if cu[1] == option_collage_name:
                # st.text(cu[0])
                st.text('')
                # collage_id = cu[0]
                # st.text(cu[0])
                return cu[0]
    # st.text(type(collage_id))
    # return collage_id


# 判断是否勾选了显示图片，如果是，那么显示，没勾选就不显示，填入值为图片的url
def show_image(image_url=''):
    if image_url == '' or len(image_url) == 0 or image_url == [] or image_url == '[]':
        pass
    else:
        st.text('- ' * 10)
        st.image(image_url, width=350, output_format="auto")

    # if image_url != '' or image_url != [] or image_url != '[]' or  image_url != None:
    #
    #     st.text(image_url)
    #     st.text(len(image_url))
    # if len(image_url) == 0:
    #     return []
    # else:
    #     st.button(image_url)


# 输入lesson_id,[1为直播，2为回放]返回qi_id和qi_name,直播和回放用
def get_qi_id(lesson_id='', live_play=1):
    if lesson_id == '' or lesson_id == [] or lesson_id == '[]' or lesson_id == None:
        return []
    else:
        if live_play == 1:
            cur = conn.execute(f"select * from qi_id_live  where lesson_id='{lesson_id}';").fetchall()
            # if cur != [] != '' != None:
            return cur

        elif live_play == 2:
            cur = conn.execute(f"select * from qi_id_play  where lesson_id='{lesson_id}';").fetchall()
            return cur
        # else:

        else:
            return []


# 返回qi_id,录播直接返回
def lesson_infos(collage_id=''):
    if collage_id == '':
        return []
    else:
        cur = conn.execute \
            (f"select * from Type_Of_Lessons  where collage_id='{collage_id}' group by lesson_id;").fetchall()
        lesson_info = cur
        # st.text(lesson_info)
        # st.text(lesson_info)
        # lesson_info, less_id, less_name, less_pic, colllage_name, collage_id
        if len(lesson_info) == 0:
            return []
        else:
            # is_show_image = st.checkbox('是否需要显示图片')
            lpr = st.radio(  # LivePlayRrec
                "选择一个展示课程的方式",
                ('直播', '回放', '录播'))

            if lpr == '直播':
                # qi_id = ''
                show_name = []
                show_name_infos = []
                for one_less in lesson_info:
                    cur = conn.execute(f"select * from qi_id_live  where lesson_id='{one_less[0]}';").fetchall()
                    qi = cur
                    if len(qi) == 0:
                        pass
                    else:
                        show_name.append(one_less[1])
                        show_name_infos.append([one_less[0], one_less[1]])
                # st.text(show_name)
                less_opt = st.selectbox('', (show_name))
                for aa in show_name_infos:
                    if aa[1] == less_opt:
                        return aa[0]


            elif lpr == '回放':
                # qi_id = ''
                show_name = []
                show_name_infos = []
                for one_less in lesson_info:
                    cur = conn.execute(f"select * from qi_id_play  where lesson_id='{one_less[0]}';").fetchall()
                    qi = cur
                    if len(qi) == 0:
                        pass
                    else:
                        show_name.append(one_less[1])
                        show_name_infos.append([one_less[0], one_less[1]])
                # st.text(show_name)
                less_opt = st.selectbox('', (show_name))
                for aa in show_name_infos:
                    if aa[1] == less_opt:
                        return aa[0]
            elif lpr == '录播':
                is_show_image = st.checkbox('是否需要显示图片')
                # show_name = []
                # show_name_infos = []
                less_id = lesson_info[0]
                list_less_name = []
                list_zhang_name = []
                for one_less in lesson_info:
                    cur = conn.execute \
                        (f"select lesson_id,lesson_name,zhang_title from lubo  where lesson_id='{one_less[0]}'group by zhang_title;").fetchall()
                    lus = cur
                    if len(lus) == 0:
                        pass
                    else:
                        list_less_name.append(lus[0][1])
                        # for aa in lus:
                        #     # st.text(aa)
                        #     pass
                opt_less_name = st.selectbox('', list_less_name)

                cur = conn.execute \
                    (f"select zhang_title,jie_title,vid_title,vid,download_url,download_name from lubo  where lesson_name='{opt_less_name}';").fetchall()
                if len(cur) == 0:
                    return 'lubo'
                else:
                    if is_show_image:
                        image_image = conn.execute(
                            f"select lessons_picture from Type_Of_Lessons  where lesson_name='{opt_less_name}'group by lessons_picture;").fetchall()[
                            0][0]
                        # st.text(image_image)
                        show_image(image_url=image_image)
                    v_infos = []
                    # st.text(v_infos)

                    for bb in cur:
                        temp = "https://hls.videocc.net/" + bb[3][0:10] + "/" + bb[3][-3] + "/" + bb[3][0:-1] + str \
                            (1) + '.m3u8'
                        v_infos.append([bb[0], bb[1], bb[2], temp, bb[4], bb[5]])
                    import pandas as pd
                    ins = []
                    JiShu_ins = 1
                    for iins in range(len(v_infos)):
                        ins.append(str(JiShu_ins))
                        JiShu_ins = JiShu_ins + 1
                    # st.text(len(ins))
                    clm = ["章节名称", "每节课名称", "视频名称", "视频地址[最低画质]", "资源地址", "资源备注"]
                    df = pd.DataFrame(v_infos, index=ins, columns=clm)
                    st.text('共计：' + str(len(v_infos)) + '条记录')
                    st.dataframe(df)
                    return 'lubo'
            else:
                return []


# 运行
def runn_ing():
    # 用户选择的collage_id
    coll_id = collage_infos_id()
    if coll_id == []:
        pass
    else:
        # 用户选择的lesson_id
        lesson_id = lesson_infos(collage_id=coll_id)
        if lesson_id == [] or lesson_id == None:
            st.text('无数据，请选择另一个展示课程的方式')
            pass
        else:
            if lesson_id == 'lubo':
                pass
            else:

                st.text(lesson_id)

        # if lesson_id == []:
        #     pass
        # else:
        #     st.text('有数据')


if __name__ == '__main__':
    # runn_ing()
    import streamlit as st
    import os
    import sqlite3

    # from io import StringIO
    # from io import BytesIO

    # 设置网页名称

    st.set_page_config(page_title='自建大鹏课程查询')
    # st.title('仅供学习使用')
    # st.write('''查询''')
    # 设置网页标题
    st.header('仅供学习使用\n使用中造成的任何问题，后果自负，否则请关闭本软件')
    st.markdown('''#### [By:开心ucu](https://www.ucu520.top)''')
    agree = st.checkbox('我同意：我本人之后的任何操作与作者[开心ucu]无关，产生的任何后果由我自行承担')
    st.write('您已同意后果自负，请合理使用!')
    # st.markdown('''####''')
    # st.text('')
    # 设置网页子标题
    # st.subheader('获取已爬取到的数据')
    st.subheader('\n')
    if agree:
        if os.path.exists('dapeng.db'):
            conn = sqlite3.connect('dapeng.db')

        else:

            # while True:
            #     from tkinter import messagebox
            #     messagebox.showerror(title="警告⚠", message="由于没找到数据库文件，请手动选择一个,点击确认后开始选择")
            #     import tkinter as tk
            #     from tkinter import filedialog
            #     root = tk.Tk()
            #     root.withdraw()
            #     f_path = filedialog.askopenfilename(typevariable='db')
            #
            #     print(f_path)
            #     if f_path != None and f_path[-2:] == 'db':
            #         break
            # conn = sqlite3.connect(f_path)

            uploaded_file = st.file_uploader('由于没找到数据库文件，请手动选择一个', type="db",accept_multiple_files=False,key="1",help="请选择数据库文件'dapeng.db',如果没有，请运行爬取的相关程序",)
            if uploaded_file is not None:
                open('dapeng.db', 'wb').write(uploaded_file.getvalue())

            conn = sqlite3.connect('dapeng.db')
            # st.text(uploaded_file)
            # file_path = "d:/"
            # uploaded_file = st.file_uploader('由于没找到数据库文件，请手动选择一个', accept_multiple_files=False)
            # print(type(uploaded_file.getvalue()))
            # open('aaa.db', 'wb').write(uploaded_file.getvalue())
            # st.text(uploaded_file.getvalue())
        try:
            runn_ing()
        except:
            pass
    #
    # if uploaded_file == None:
    #     pass
    # else:
    #     bytes_data = uploaded_file.read1()
    #     # st.write("filename:", uploaded_file.name)
    #     st.text(type(bytes_data))

    # st.write(bytes_data.decode())

    # st.write(bytes_data)

    # st.text(into_files)
    # if into_files != None:
    #
    #     aaaaaaa = StringIO(into_files.read())
    #     conn = sqlite3.connect(aaaaaaa)

    # filename = st.file_picker("Pick a file", folder="my_folder", type=("png", "jpg"))
    # file_bytes = st.file_uploader("Upload a file", type=("png", "jpg"))

    # tsts = file = st.file_uploader('')
    # if tsts == None:
    #     pass
    # else:
    #
    #     with open(tsts, 'r', encoding='utf-8') as f:
    #         st.text(tsts.read())

    # if files_local == None:
    #     st.text('请选择数据库文件')
    # else:
    #
    #
    #     import sqlite3
    #
    #     conn = sqlite3.connect(files_local.read())
    #     runn_ing()
