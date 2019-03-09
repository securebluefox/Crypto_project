# -*- coding: UTF-8 -*-
import Playfair,Vigenere,Hill


def playfair_menu():
    while True:
        print("-----Playfair密码-----")
        print("请选择你要进行的操作：")
        print("1.Playfair密码简介")
        print("2.Playfair密码加密")
        print("3.Playfair密码解密")
        print("4.返回上一级")
        crypto_operating = input("->")
        if crypto_operating == '1':
            Playfair.playfair_info()
        elif crypto_operating == '2':
            print("-----------------Playfair密码加密---------------")
            print("请输入您的明文：（加密结束后会丢失大小写与空格）")
            plain_text = input()
            print("请输入您的密钥：")
            key = input()
            print("加密正在进行。。。")
            print("加密成功！")
            print("密文为：" + Playfair.playfair_encrypt(plain_text, key))
        elif crypto_operating == '3':
            print("-----------------Playfair密码解密---------------")
            print("请输入您的密文：")
            enc_text = input()
            print("请输入您的密钥：")
            key = input()
            print("解密正在进行。。。")
            info = Playfair.playfair_decrypt(enc_text, key)
            if info == 40001:
                print("解密失败！")
                print("错误码：40001，请检查密文长度！密文必须为偶长度！")
            else:
                print("解密成功！（大小写与空格需要自行根据语义恢复）")
                print("明文为：" + info)
        elif crypto_operating == '4':
            return
        else:
            print("选择出错！")


def vigenere_menu():
    while True:
        print("-----Vigenere密码-----")
        print("请选择你要进行的操作：")
        print("1.Vigenere密码简介")
        print("2.Vigenere密码加密")
        print("3.Vigenere密码解密")
        print("4.返回上一级")
        crypto_operating = input("->")
        if crypto_operating == '1':
            Vigenere.vigenere_info()
        elif crypto_operating == '2':
            print("-----------------Vigenere密码加密---------------")
            print("请输入您的明文：")
            plain_text = input()
            print("请输入您的密钥：(密钥应为合法英文单词)")
            key = input()
            print("加密正在进行。。。")
            print("加密成功！")
            print("密文为：" + Vigenere.vigenere_encrypt(plain_text, key))
        elif crypto_operating == '3':
            print("-----------------Vigenere密码解密---------------")
            print("请输入您的密文：")
            enc_text = input()
            print("请输入您的密钥：(密钥应为合法英文单词)")
            key = input()
            print("解密正在进行。。。")
            print("解密成功！")
            print("明文为：" + Vigenere.vigenere_decrypt(enc_text, key))
        elif crypto_operating == '4':
            return
        else:
            print("选择出错！")


def hill_menu():
    while True:
        print("-----Hill密码-----")
        print("请选择你要进行的操作：")
        print("1.Hill密码简介")
        print("2.Hill密码加密")
        print("3.Hill密码解密")
        print("4.返回上一级")
        crypto_operating = input("->")
        if crypto_operating == '1':
            Hill.hill_info()
        elif crypto_operating == '2':
            print("----------------------Hill密码加密----------------------")
            print("请输入您的明文：（加密结束后会丢失大小写与空格）")
            plain_text = input()
            print("请输入您的密钥：(密钥应为一系列数字，空格分隔，依次输入)")
            key = input()
            print("请输入您的密钥阶数：")
            n = input()
            print("加密正在进行。。。")
            print("加密成功！")
            print("密文为：" + Hill.hill_encrypt(plain_text, key.split(),int(n)))
        elif crypto_operating == '3':
            print("----------------------Hill密码加密----------------------")
            print("请输入您的密文：")
            enc_text = input()
            print("请输入您的密钥：(密钥应为一系列数字，空格分隔，依次输入)")
            print("(密钥应为加密时使用的密钥)")
            key = input()
            print("请输入您的密钥阶数：")
            n = input()
            print("解密正在进行。。。")
            print("解密成功！（大小写与空格需要自行根据语义恢复）")
            print("明文为：" + Hill.hill_decrypt(enc_text, key.split(),int(n)))
        elif crypto_operating == '4':
            return
        else:
            print("选择出错！")


def main_menu():
    while True:
        print("--------主菜单--------")
        print("请选择你要使用的密码：")
        print("1.Playfair密码")
        print("2.Vigenere密码")
        print("3.Hill密码")
        print("4.退出")
        crypto_type = input("->")
        if crypto_type == '1':
            playfair_menu()
        elif crypto_type == '2':
            vigenere_menu()
        elif crypto_type == '3':
            hill_menu()
        elif crypto_type == '4':
            return
        else:
            print("选择出错！")


if __name__ == "__main__":
    main_menu()
