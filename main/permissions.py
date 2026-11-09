"""Permission class DRF untuk API portofolio.

Autentikasi (siapa pengirimnya) ditangani SessionAuthentication; kelas di sini
hanya memutuskan otorisasi (bolehkah tindakan ini dilakukan), sebelum isi view
dijalankan.
"""

from rest_framework.permissions import BasePermission, SAFE_METHODS

EDITOR_GROUP = "Editor"


class IsPortfolioOwnerOrReadOnly(BasePermission):
    """Semua orang boleh membaca; hanya superuser (pemilik) yang boleh menulis."""

    message = "Only the portfolio owner can change projects."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    """Hak akses empat peran dari Tugas 4.

    - Pengunjung dan pengguna biasa: hanya GET/HEAD/OPTIONS.
    - Editor (anggota grup "Editor"): ditambah PUT/PATCH.
    - Pemilik (superuser): semua method, termasuk POST dan DELETE.
    Star tidak diatur di sini; endpoint star memakai IsAuthenticated.
    """

    message = "Hanya pemilik yang dapat menambah atau menghapus data; Editor hanya dapat mengubahnya."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return (
            request.method in ("PUT", "PATCH")
            and request.user.groups.filter(name=EDITOR_GROUP).exists()
        )
