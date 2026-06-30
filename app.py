from flask import Flask, render_template, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

@app.route('/')
def index():
    """الصفحة الرئيسية"""
    return app.send_static_file('index.html')

@app.route('/api/services', methods=['GET'])
def get_services():
    """الحصول على قائمة الخدمات"""
    services = [
        {
            'id': 1,
            'name': 'تأسيس المتجر الإلكتروني',
            'description': 'إنشاء متجر إلكتروني احترافي من الصفر',
            'icon': '🏪'
        },
        {
            'id': 2,
            'name': 'تطوير وتحسين الأداء',
            'description': 'تحسين سرعة وأداء المتجر',
            'icon': '⚡'
        },
        {
            'id': 3,
            'name': 'التسويق الرقمي',
            'description': 'استراتيجيات تسويق فعّالة لزيادة المبيعات',
            'icon': '📱'
        },
        {
            'id': 4,
            'name': 'إدارة المحتوى',
            'description': 'إدارة وتحديث محتوى المتجر بانتظام',
            'icon': '📝'
        },
        {
            'id': 5,
            'name': 'تحليل البيانات',
            'description': 'تحليل أداء المتجر واستخراج التقارير',
            'icon': '📊'
        },
        {
            'id': 6,
            'name': 'دعم العملاء',
            'description': 'دعم فني 24/7 لضمان سير العمل بسلاسة',
            'icon': '💬'
        },
        {
            'id': 7,
            'name': 'التدريب والاستشارات',
            'description': 'تدريب فريقك على إدارة المتجر',
            'icon': '🎓'
        },
        {
            'id': 8,
            'name': 'تطبيقات الجوال',
            'description': 'تطوير تطبيقات جوال للمتجر الإلكتروني',
            'icon': '📲'
        }
    ]
    return jsonify(services)

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """الحصول على الإحصائيات"""
    stats = {
        'stores_launched': 30,
        'conversion_rate': 70,
        'services': 8,
        'vision_year': 2030
    }
    return jsonify(stats)

@app.route('/api/contact', methods=['POST'])
def contact_form():
    """معالجة نموذج التواصل"""
    from flask import request
    
    data = request.get_json()
    
    # معالجة البيانات
    response = {
        'success': True,
        'message': 'تم استقبال رسالتك بنجاح، سيتم التواصل معك قريباً'
    }
    
    return jsonify(response)

@app.errorhandler(404)
def not_found(error):
    """معالجة الأخطاء 404"""
    return jsonify({'error': 'الصفحة غير موجودة'}), 404

@app.errorhandler(500)
def server_error(error):
    """معالجة أخطاء الخادم"""
    return jsonify({'error': 'حدث خطأ في الخادم'}), 500

if __name__ == '__main__':
    # تشغيل الخادم
    # للإنتاج استخدم WSGI server مثل Gunicorn
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=os.environ.get('FLASK_ENV') == 'development'
    )
