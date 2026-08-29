global_var = 100  #  Global Scope متاح في كل مكان

def my_function():
    local_var = 50  # Local Scope  يعيش فقط داخل الدالة
    print(f"Inside function: local={local_var}, global={global_var}")

my_function()

# محاولة الوصول للمتغير المحلي من الخارج تسبب خطأ NameError
# print(local_var)
