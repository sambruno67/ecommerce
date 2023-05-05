from django.contrib import admin
from .models import Category, Product, Commande

# Register your models here.

admin.site.site_header = "Mon site Ecommerce"
admin.site.site_title = "Administration SamShop"
admin.site.index_title = "Administration SamShop"

class AdminCategory(admin.ModelAdmin) :
    list_display = ('name', 'date_added')
    search_fields = ('name',)
    

class AdminProduct(admin.ModelAdmin) :
    list_display = ('title', 'price', 'category', 'date_added', 'image')
    list_filter = ('category',)
    search_fields = ('title',)
    list_editable = ('price',)

class AdminCommande(admin.ModelAdmin) :
    list_display = ('items', 'email', 'adresse', 'ville', 'pays','total', 'date_commande')
    search_fields = ('email','adresse', 'ville', 'pays', )


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Commande, AdminCommande)
