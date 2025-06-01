# AutoMailer 📬

AutoMailer 是一個簡單的 Python CLI 工具，支援 Gmail SMTP 發送 Email。  
使用者可以透過終端機互動輸入收件人、主旨與內容，程式會自動完成寄信流程。

## 功能介紹

- 自訂收件人、主旨與內容
- 使用 Gmail 應用程式密碼進行 SMTP 驗證
- 採用 SSL 加密連線（smtplib + email.message）

## 使用方式

```bash
python send_mail.py
