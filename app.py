from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
# Secret key untuk flash messages dan session
app.secret_key = 'fashion_store_secret_key_123'

# Memastikan folder templates ada
if not os.path.exists('templates'):
    os.makedirs('templates')

# Route untuk halaman utama
@app.route('/')
def home():
    # Data produk (bisa diganti dengan database nantinya)
    products = [
        {
            'id': 1,
            'name': 'Kemeja Casual',
            'price': 199000,
            'image': '/api/placeholder/400/300'
        },
        {
            'id': 2,
            'name': 'Dress Modern',
            'price': 299000,
            'image': '/api/placeholder/400/300'
        },
        {
            'id': 3,
            'name': 'Kaos Premium',
            'price': 149000,
            'image': '/api/placeholder/400/300'
        }
    ]
    return render_template('index.html', products=products)

# Route untuk handling form kontak
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Di sini Anda bisa menambahkan logika untuk menyimpan pesan
        # ke database atau mengirim email
        
        # Menambahkan flash message
        flash('Pesan Anda telah terkirim! Kami akan segera menghubungi Anda.', 'success')
        
        return redirect(url_for('home', _anchor='contact'))

# Route untuk handling pembelian produk
@app.route('/buy/<int:product_id>', methods=['POST'])
def buy_product(product_id):
    # Di sini Anda bisa menambahkan logika untuk proses pembelian
    flash('Produk telah ditambahkan ke keranjang!', 'success')
    return redirect(url_for('home', _anchor='products'))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Pastikan file index.html ada di folder templates
    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    if not os.path.exists(os.path.join(template_path, 'index.html')):
        print("Error: index.html tidak ditemukan di folder templates!")
        exit(1)
    
    # Menjalankan aplikasi dalam mode debug
    app.run(debug=True)