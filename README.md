## 生成二维码转化为png base64

-. 使用qrcode

  qrcode 依赖PIL
       python3安装PIL：pip install PIL
       python2安装PIL：pip install pillow

-. base64
   import cStringIO
   import base64
    # 依赖StringIO容器装载二维码
    jpeg_image_buffer = cStringIO.StringIO()
    img.save(jpeg_image_buffer, format="PNG")
    imgStr = base64.b64encode(jpeg_image_buffer.getvalue())

    qrcode 生成的二维码sava输出到stringIO中

-. base64解析

   base64 的图片 在网页中解析：
        <img src="data:image/jpg;base64,base64编码图片后的sting"/>

