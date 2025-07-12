
import os
from modules.validator import validate_national_code, validate_passport_number, validate_phone_number
from modules.excel_writer import append_to_excel
from modules.ocr_passport import check_passport_validity
from dotenv import load_dotenv

# فرضی: اینجاست که به API پیام‌رسان بله وصل می‌شیم
# from balebot import BaleBot, Message

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def start_bot():
    print("🤖 ربات بله فعال شد. منتظر پیام کاربران هستیم...")

    user_data = {}

    print("👋 خوش آمدید به ربات رسمی ثبت‌نام کاروان زیارتی یاران.")

    user_data['name'] = input("📝 لطفاً نام و نام خانوادگی خود را وارد کنید: ")

    code = input("🆔 لطفاً کد ملی خود را وارد کنید: ")
    while not validate_national_code(code):
        code = input("❌ کد نامعتبر است! لطفاً مجدداً کد ملی را وارد کنید: ")
    user_data['کد ملی'] = code

    phone = input("📱 لطفاً شماره تلفن همراه را وارد کنید: ")
    while not validate_phone_number(phone):
        phone = input("❌ شماره نامعتبر است! لطفاً مجدداً شماره تلفن را وارد کنید: ")
    user_data['شماره تلفن'] = phone

    passport = input("🛂 لطفاً شماره گذرنامه را وارد کنید: ")
    while not validate_passport_number(passport):
        passport = input("❌ شماره گذرنامه نامعتبر است! لطفاً دوباره وارد کنید: ")
    user_data['شماره گذرنامه'] = passport

    pass_img = input("🖼️ لطفاً مسیر عکس صفحه اول گذرنامه را وارد کنید (مثال: passport.jpg): ")
    if check_passport_validity(pass_img):
        print("✅ گذرنامه معتبر است.")
    else:
        print("⚠️ هشدار: تصویر گذرنامه ممکن است نامعتبر باشد.")
    user_data['تصویر گذرنامه'] = pass_img

    photo = input("📸 لطفاً مسیر عکس پرسنلی ۳×۴ خود را وارد کنید (مثال: photo.jpg): ")
    user_data['عکس پرسنلی'] = photo

    append_to_excel(user_data)

    print("\n✅ ثبت‌نام با موفقیت انجام شد.")
    print("💬 مبلغ تور متعاقباً اعلام خواهد شد. با تشکر از همراهی شما.")

if __name__ == "__main__":
    start_bot()
