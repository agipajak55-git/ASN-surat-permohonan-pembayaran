# -*- coding: utf-8 -*-
{
    'name': 'Surat Permohonan Pembayaran Sales Order (ASN)',
    'version': '16.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Cetak Surat Permohonan Pembayaran PT. AGI SOLUSI NEGERI dari Sales Order (Odoo 16 Community)',
    'description': """
Module Konversi Generator Surat Permohonan Pembayaran ke Odoo 16 Community - PT. AGI SOLUSI NEGERI
===================================================================================================
Fitur:
- Mengambil tanggal surat & nomor surat (bulan romawi & tahun) dari field 'Tanggal Print' (tanggal_print).
  Jika tanggal_print kosong, otomatis fallback ke tanggal hari ini.
- Lampiran Faktur Pajak bersifat opsional via checkbox 'Lampirkan Faktur Pajak' pada Sales Order:
  * Dicentang: 4 berkas (Invoice, Kuitansi, Faktur Pajak, Salinan dasar) & baris potongan pajak dimunculkan.
  * Tidak dicentang: 3 berkas (tanpa Faktur Pajak) & baris potongan pajak disembunyikan.
- Checkbox 'Pakai Meterai': mengatur jarak tanda tangan 30mm (pakai meterai) atau 10mm (tanpa meterai).
- Penomoran otomatis format: [nomor SO]/Perm.Bayar/ASN/[bulan romawi]/[tahun]
- Terbilang otomatis Bahasa Indonesia (Rupiah).
- Rincian Bank Mandiri KCP Solo Pasar Legi ASN (138 00 5830000 0), tata letak presisi sesuai kop surat & generator HTML.
    """,
    'author': 'PT. AGI SOLUSI NEGERI',
    'website': 'https://www.astongraphindo.com',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'account',
    ],
    'data': [
        'views/sale_order_views.xml',
        'report/report_surat_permohonan_pembayaran.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
