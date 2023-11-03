from gmssl import sm2, sm3, func

# 生成SM2密钥对
sm2_crypt = sm2.CryptSM2(
    public_key='04EBFC718E8D1798620432268DF0B7F6F5D699366E4F9ECCC98E16EAC8EA28B4B4C6F6FF7C8AB9A3E04BE86F8A6FE954A151B7329D8F5C21A9C350E269EA37E1AE',
    private_key='395F9F7FE039321C7884F0368E51C9D0DCE68F4737AEC0AF32F611AF82E1F26B')
# 生成SM3哈希值
sm3_hash = sm3.sm3_hash(func.bytes_to_list(b"Hello world"))

# 定义邮件内容
message = "这是一封测试邮件"

# 对邮件内容进行加密
enc_data = sm2_crypt.encrypt(message.encode())

# 对加密后的邮件内容进行数字签名
K = '00F5A03B8EE9E0CBD830473D06758978F4E68FB6B545F2B1F3AA227CEC232FC3'
sign = sm2_crypt.sign(sm3_hash.encode(), K)

# 对加密后的邮件内容进行解密
dec_data = sm2_crypt.decrypt(enc_data).decode()

# 对解密后的邮件内容进行验证签名
verify = sm2_crypt.verify(sign, sm3_hash)

# 打印结果
print("原始邮件内容：", message)
print("加密后的邮件内容：", enc_data)
print("数字签名：", sign)
print("解密后的邮件内容：", dec_data)
print("验证签名结果：", verify)
