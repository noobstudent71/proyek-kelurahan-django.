document.addEventListener('DOMContentLoaded', () => {
    const wargaListContainer = document.getElementById('warga-list-container');
    const formTambahWarga = document.getElementById('form-tambah-warga'); // Ambil elemen form
    const apiUrl = 'http://127.0.0.1:8000/api/warga/';
    
    // --- GANTI INI DENGAN TOKEN ADMIN ANDA DARI THUNDER CLIENT ---
    const YOUR_TOKEN = 'Token 6d5ff83988a6e197f93335fc05dd88297ef0061f'; 
    // Contoh: 'Token 59e5f1a349f19a9cd7d1030c1c230066f548427d'
    // -----------------------------------------------------------

    // Fungsi 1: Menampilkan Data (GET)
    function fetchWarga() {
        wargaListContainer.innerHTML = '<p>Sedang memuat ulang data...</p>';
        
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                wargaListContainer.innerHTML = ''; // Bersihkan container
                
                // Cek apakah data ada
                if (data.results && data.results.length > 0) {
                    data.results.forEach(warga => {
                        const div = document.createElement('div');
                        div.className = 'warga-item';
                        div.innerHTML = `
                            <h3>${warga.nama_lengkap}</h3>
                            <p><strong>NIK:</strong> ${warga.nik}</p>
                            <p><strong>Alamat:</strong> ${warga.alamat}</p>
                            <p><strong>Telp:</strong> ${warga.no_telepon || '-'}</p>
                        `;
                        wargaListContainer.appendChild(div);
                    });
                } else {
                    wargaListContainer.innerHTML = '<p>Belum ada data warga.</p>';
                }
            })
            .catch(error => console.error('Error:', error));
    }

    // Fungsi 2: Menambah Data Baru (POST) - TUGAS CHALLENGE
    formTambahWarga.addEventListener('submit', (e) => {
        e.preventDefault(); // Mencegah halaman refresh otomatis

        // Ambil nilai dari input HTML
        const dataBaru = {
            nama_lengkap: document.getElementById('nama_lengkap').value,
            nik: document.getElementById('nik').value,
            alamat: document.getElementById('alamat').value,
            no_telepon: document.getElementById('no_telepon').value
        };

        // Kirim ke API menggunakan Fetch
        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': YOUR_TOKEN // Wajib untuk izin akses
            },
            body: JSON.stringify(dataBaru)
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Gagal menyimpan data (Cek Token atau validasi data)');
            }
        })
        .then(data => {
            alert('Berhasil menambah warga: ' + data.nama_lengkap);
            formTambahWarga.reset(); // Kosongkan form
            fetchWarga(); // Refresh daftar warga otomatis
        })
        .catch(error => {
            alert(error.message);
            console.error('Error:', error);
        });
    });

    // Panggil fungsi fetch pertama kali saat halaman dibuka
    fetchWarga();
});