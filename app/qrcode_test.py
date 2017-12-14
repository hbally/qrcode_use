# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 10:00
# @Author  : Ayan
# @Email   : hbally
# @File    : qrcode_test.py
# @Software: PyCharm


def make_png():
    '''使用qrcode生成二维码图片png 或者其他格式
       qrcode 依赖PIL
       python3安装PIL：pip install PIL
       python2安装PIL：pip install pillow
    '''
    import qrcode
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # 目标url
    qr.add_data('Some data')
    qr.make(fit=True)

    # url 转二维码
    img = qr.make_image()
    # 输出二维码到文件
    img.save('qrcode_tmp.png')


def make_base64():
    '''png图片转bese64'''
    import base64
    with open("qrcode_tmp.png", "rb") as f:
        base_str = base64.b64encode(f.read())
        print base_str
        '''
         iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKAQAAAABTUiuoAAACBklEQVR4nO3bQY6bMBTG8f 
         + rkVgaaQ4wRzE3q3qk3gAONBJeVgJ9XdiQZKatwlQkVH3eBMhv8UmWyfOzYuLOMX65V4JTp06dOnV6JLU6GoDFrGcx6 
         / P6uD88gNM9NEmSJmC0VvpmrYAgSdItPSaA03tGUz9zB 
         + k7kARGfDORwSDMhwZw + hfUeoA0BZWrhwdw + ofRvH8wdhOC5cMXz8 
         / qdJ2UKCBTJyoNoHp7cACn + +loZmYdWJ9bQW5lPUspCR8RwOk9o6ytyxISeTGRF6vr7egATj 
         + x3 + ooC4zxdQZirdvLF8cHcHrX2Cp4Q8QJIwYZcQLyy3xNn57VKWUDPJTFFCRNQRoAiDOS5rp3Hp6e1SlrtyKIpO0lGKV1Gud1Qp 
         + e1ekNza00sBhbsxAI3nk6G03TYhBn7OtUX4eQm1 / RYwI43UtHa4Bcm + 4
        aCCJNi / fgz0eDIM6U2mJgMcZuMetzQy06zpP1v6VXLzuRbbsJKtdjF2ZLw3EBnO6mGuJWDuZWpd 
        + UJJH0wztPJ6Pvzo7LLovclMPJBwRwuodenR2 / Smbd5WfM19Z5aN0dp4lyBrlWghcQ5Lvj09I0UYvA7cr6RwZw 
        + vvx8YiYxUjD3GjsgNLfPTCA00 / M1np2bAAivwji281cPj2r0zofYyklAmUxjX0oz414cACnO6j5vxacOnXq1Ok 
        / RH8CE8rxK7alsh8AAAAASUVORK5CYII =

        '''


def make_buffer_base64():
    '''
    qrcode url -> 二维码 -> string
    '''
    import qrcode
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # input  url
    qr.add_data('Some data')
    qr.make(fit=True)

    # make 二维码
    img = qr.make_image()

    # output string
    import cStringIO
    import base64
    # 依赖StringIO容器装载二维码
    jpeg_image_buffer = cStringIO.StringIO()
    img.save(jpeg_image_buffer, format="PNG")
    imgStr = base64.b64encode(jpeg_image_buffer.getvalue())
    print imgStr
    '''
    iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKAQAAAABTUiuoAAACBklEQVR4nO3bQY6bMBTG8f 
    + rkVgaaQ4wRzE3q3qk3gAONBJeVgJ9XdiQZKatwlQkVH3eBMhv8UmWyfOzYuLOMX65V4JTp06dOnV6JLU6GoDFrGcx6 
    / P6uD88gNM9NEmSJmC0VvpmrYAgSdItPSaA03tGUz9zB + k7kARGfDORwSDMhwZw + hfUeoA0BZWrhwdw + ofRvH8wdhOC5cMXz8 
    / qdJ2UKCBTJyoNoHp7cACn + +loZmYdWJ9bQW5lPUspCR8RwOk9o6ytyxISeTGRF6vr7egATj + x3 + 
    ooC4zxdQZirdvLF8cHcHrX2Cp4Q8QJIwYZcQLyy3xNn57VKWUDPJTFFCRNQRoAiDOS5rp3Hp6e1SlrtyKIpO0lGKV1Gud1Qp 
    + e1ekNza00sBhbsxAI3nk6G03TYhBn7OtUX4eQm1 / RYwI43UtHa4Bcm + 4
    aCCJNi / fgz0eDIM6U2mJgMcZuMetzQy06zpP1v6VXLzuRbbsJKtdjF2ZLw3EBnO6mGuJWDuZWpd + UJJH0wztPJ6Pvzo7LLovclMPJBwRwuodenR2 
    / Smbd5WfM19Z5aN0dp4lyBrlWghcQ5Lvj09I0UYvA7cr6RwZw + vvx8YiYxUjD3GjsgNLfPTCA00 
    / M1np2bAAivwji281cPj2r0zofYyklAmUxjX0oz414cACnO6j5vxacOnXq1Ok 
    / RH8CE8rxK7alsh8AAAAASUVORK5CYII =
    
    base64 的图片 在网页中解析：
        <img src="data:image/jpg;base64,base64编码图片后的sting"/>

    '''


if __name__ == "__main__":
    # make_base64()
    make_buffer_base64()
