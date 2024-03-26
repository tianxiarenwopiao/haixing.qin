# -*- 编码：utf-8 -*-
”“”
创建于 2024 年 1 月 11 日星期四 14:30:52

@作者：zijie.xu
”“”
导入sklearn
从sklearn.ensemble导入RandomForestRegressor  
将streamlit导入为st
将pandas导入为pd
将numpy导入为np

从PIL导入图像
进口泡菜
导入操作系统

导入请求
#url = 'https://gitee.com/zijiexu/work/raw/master/rrmodel.dat'
url = 'https://gitee.com/qin-haixing/sailun/raw/master/model.dat'
r=请求。获取（网址）
将 open ( 'rr1.dat' , 'wb' ) 作为f：
    F。写（ r.内容）
  # f.close
当前目录 = 操作系统。获取cwd ( )
完整路径 = os. 小路。加入（当前目录，'rr1.dat' ）

load_model=pickle.load_model=泡菜。加载模型=pickle. load_model =pickle。加载（打开（完整路径，“rb”））
#url1 = 'https://gitee.com/zijiexu/work/raw/master/2.jpg'
url1 = 'https://gitee.com/qin-haixing/sailun/raw/master/Figure.jpg'
r1=请求。获取（网址1 ）
（'rr.jpg'，'wb'）作为f1：
    f1。写（ r1.内容）
  # f.close
full_path1 = 操作系统。小路。加入（当前目录，'rr.jpg'）


英石。title  ( “轮胎RR值预测”)
第1行 =圣。列(  2  )
第2行 =圣。列(  2  )
第3行 =圣。列(    2    )
输入数据=pd.数据框(    )
输出数据=pd.数据框(    )
df=pd.数据框(    )

方均根托盘= 0.30      #
rsq= 0.990     #

与行1 [   0  ]：
    与圣。容器（）：
        上传的文件 = st。file_uploader ( "选择一个文件" ,label_visibility= "折叠" )
        如果uploaded_file不是 None：  ​ 
            # Can be used wherever a "file-like" object is accepted:
            input_data = pd.read_csv(uploaded_file,delimiter='	')
            inputdata=np.array(input_data)
            output_data=[load_model.predict(inputdata),load_model.predict(inputdata)/inputdata[:,-2]*1000]
            output_data=np.array(output_data).T
    with st.container():
        st.dataframe(input_data)
with row1[1]:
    with st.container():
        st.write('RMSE(均方根误差,N/KN）：%.2f'%rmse)
        st.write('模型测试值与预测值相关性系数R^2：%.2f'%rsq)
        if st.button('滚动阻力预测'):
            
            df = pd.DataFrame(output_data,columns=('Fx, N','RR, N/kN'))
    with st.container():
        st.dataframe(df)
with row2[0]:
    with st.container():
        IMG = Image.open(full_path1)
        st.image(IMG)
with row2[1]:
    with st.container():
        st.write('免责声明：')
        st.write('1.本模型适用规格为R16、R17和R18；')
        st.write('2.建模的基础数据均为非液体黄金胶种；')
        st.write('3.模型的RMSE使用15组数据进行计算（每个规格各5组）；')
        st.write('4.此预测结果供使用人员筛选方案与结果预测使用；对于个别异常数据请及时与秦海兴直接联系。')
        st.write('版本号：RRP.1.1.1')
    
        
