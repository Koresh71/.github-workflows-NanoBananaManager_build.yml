# --- РАЗДЕЛ 1: ИМПОРТЫ И ПЛАТФОРМОЗАВИСИМЫЕ НАСТРОЙКИ --- # 1
import tkinter as tk # 2
from tkinter import ttk, messagebox, scrolledtext, simpledialog # 3
import json, os, sys, hashlib, uuid, webbrowser, base64, glob, re, shutil # 4

import platform # 5
IS_WINDOWS = platform.system() == "Windows" # 6

if IS_WINDOWS: # 7
    if IS_WINDOWS: import ctypes # 8
    if IS_WINDOWS: import winreg # 9
    try: # 10
        from ctypes import windll # 11
        windll.shcore.SetProcessDpiAwareness(1) # 12
        myappid = 'ikdesigns.nanobananamanager.pro.1' # 13
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) # 14
    except: # 15
        pass # 16

# --- РАЗДЕЛ 2: СИСТЕМНЫЕ ФУНКЦИИ --- # 17
def resource_path(relative_path): # 18
    try: # 19
        base_path = sys._MEIPASS # 20
    except Exception: # 21
        base_path = os.path.abspath(".") # 22
    return os.path.join(base_path, relative_path) # 23

def get_base_dir(): # 24
    if getattr(sys, 'frozen', False): # 25
        return os.path.dirname(sys.executable) # 26
    return os.path.dirname(os.path.abspath(__file__)) # 27

# --- РАЗДЕЛ 3: ТЕХНИЧЕСКИЕ ДАННЫЕ И ЦВЕТОВАЯ СХЕМА --- # 28
SECRET_SALT = "BANANA-PRO-2026-KORNILOV" # 29

BG_MAIN, BG_PANEL = "#2d2d2d", "#3d3d3d" # 30
ACCENT, ACCENT_2 = "#f59e0b", "#d97706" # 31
TEXT_MAIN, TEXT_DESC, TEXT_MUTED = "#fefce8", "#e2e8f0", "#94a3b8" # 32
SUCCESS, DANGER = "#22c55e", "#ef4444" # 33

# --- РАЗДЕЛ 4: ТЕКСТОВЫЕ ДАННЫЕ И ЛОКАЛИЗАЦИЯ --- # 34
INFO_RU = """Nano Banana, — это продвинутый редактор и генератор изображений на основе искусственного интеллекта. Она основана на технологиях Google, # 35

Его часто называют «нейрофотошопом», потому что он позволяет с высокой точностью редактировать определенные области изображения, используя текстовые подсказки. # 36

Основные характеристики и возможности # 37
Итеративное редактирование: модель может вносить многоэтапные изменения, сохраняя контекст диалога и целостность изображения. # 38
Портретное сходство: оно позволяет менять одежду, фон или позы на фотографиях, сохраняя при этом лицо человека неизменным. # 39
Точность (восстановление деталей: Nano Banana точно редактирует отдельные области, изменяя логотипы, цвета и объекты, не затрагивая остальную часть изображения. # 40
Генерация: Программа может создавать изображения с нуля на основе текстового описания (преобразование текста в изображение) студийного качества.""" # 41

INFO_EN = """Nano Banana is an advanced AI-powered image editor and generator based on Google technologies. # 42

It is often called "neuro-Photoshop" because it allows for high-precision editing of specific areas of an image using text prompts. # 43

Key Features and Capabilities: # 44
• Iterative Editing: the model can make multi-step changes while preserving dialogue context and image integrity. # 45
• Portrait Fidelity: it allows changing clothes, background, or poses in photos while keeping the person's face unchanged. # 46
• Precision (Detail Restoration): Nano Banana accurately edits individual areas, changing logos, colors, and objects without affecting the rest of the image. # 47
• Generation: The program can create studio-quality images from scratch based on text descriptions.""" # 48

HELP_RU = """📝 Инструкция по использованию программы: # 49
Поиск: Во вкладке 'База Промптов' выберите категорию в списке слева. Нажмите на название эффекта. # 50
Копирование: Нажмите кнопку 'КОПИРОВАТЬ ТЕКСТ'. Текст скопируется в буфер обмена. # 51
Управление: Во вкладке 'Управление базой' можно добавлять свои наработки (+). # 52
Редактирование: Выберите свой промпт (user), измените поля и нажмите 'СОХРАНИТЬ'. # 53
База: Программа видит все файлы *_nano_prompts.ikd.""" # 54

HELP_EN = """📝 Program Usage Instructions: # 55
Search: Select a category and effect from the list on the left. Click on the name to see description. # 56
Copying: Click 'COPY TEXT' to save text to clipboard. # 57
Management: Add your own work in the 'Management' tab. Click '+' to create a category. # 58
Editing: Only user prompts can be modified. Edit fields and click 'SAVE'. # 59
Database: Automatically loads all files ending in _nano_prompts.ikd.""" # 60

LANG_DATA = { # 61
    "RU": { # 62
        "title": "Nano Banana PRO | IK Designs", # 63
        "tab_main": "💻 База Промптов", "tab_admin": "⚙ Управление базой", # 64
        "tab_info": "📖 Информация", "tab_help": "📝 Инструкция", # 65
        "nav": "🧭 НАВИГАЦИЯ", "all_cats": "Все категории", # 66
        "copy_btn": "🚀 КОПИРОВАТЬ ТЕКСТ", "save_btn": "💾 СОХРАНИТЬ", # 67
        "del_btn": "🗑 УДАЛИТЬ ПУНКТ", "add_new": "➕ ДОБАВИТЬ НОВЫЙ ПРОМТ", # 68
        "cat_label": "1. КАТЕГОРИЯ:", "name_label": "2. НАЗВАНИЕ ЭФФЕКТА:", # 69
        "desc_label": "3. ОПИСАНИЕ:", "prompt_label": "4. ПРОМПТ:", # 70
        "main_cat_head": "Категория:", "main_desc_head": "ОПИСАНИЕ (RU):", # 71
        "main_prompt_head": "ПРОМПТ (EN):", "lang_btn": "Language: EN", # 72
        "zoom_btn": "🔍 МАСШТАБ", # 73
        "about_btn": "ℹ О ПРОГРАММЕ", # 74
        "about_msg": "🍌 Nano Banana PRO\n\nВерсия: V 1.9\nЛицензия: АКТИВИРОВАНА ✅\nID: {hwid}\nРазработчик: IK Designs", # 75
        "confirm_del": "Подтверждение", "ask_del": "Вы уверены, что хотите удалить этот элемент?", # 76
        "copy_ok": "Текст скопирован!" # 77
    }, # 78
    "EN": { # 79
        "title": "Nano Banana PRO | IK Designs", # 80
        "tab_main": "💻 Prompt Database", "tab_admin": "⚙ Management", # 81
        "tab_info": "📖 Information", "tab_help": "📝 Instruction", # 82
        "nav": "🧭 NAVIGATION", "all_cats": "All Categories", # 83
        "copy_btn": "🚀 COPY TEXT", "save_btn": "💾 SAVE CHANGES", # 84
        "del_btn": "🗑 DELETE ITEM", "add_new": "➕ ADD NEW PROMPT", # 85
        "cat_label": "1. CATEGORY:", "name_label": "2. EFFECT NAME:", # 86
        "desc_label": "3. DESCRIPTION:", "prompt_label": "4. PROMPT:", # 87
        "main_cat_head": "Category:", "main_desc_head": "DESCRIPTION (EN):", # 88
        "main_prompt_head": "PROMPT (EN):", "lang_btn": "Язык: RU", # 89
        "zoom_btn": "🔍 ZOOM", # 90
        "about_btn": "ℹ ABOUT", # 91
        "about_msg": "🍌 Nano Banana PRO\n\nVersion: V 1.9\nLicense: ACTIVATED ✅\nID: {hwid}\nDeveloper: IK Designs", # 92
        "confirm_del": "Confirmation", "ask_del": "Are you sure you want to delete this item?", # 93
        "copy_ok": "Copied!" # 94
    } # 95
} # 96

# --- РАЗДЕЛ 5: ОСНОВНОЙ КЛАСС --- # 97
class NanoBananaManager: # 98
    def __init__(self, root): # 99
        self.root = root # 100
        self.current_lang = "RU" # 101
        self.zoom_scale = 1.0 # 102
        self.root.configure(bg=BG_MAIN) # 103
        
        self.base_dir = get_base_dir() # 104
        self.lic_file = os.path.join(self.base_dir, "nano_license.ikd") # 105
        self.user_data_file = os.path.join(self.base_dir, "user_nano_prompts.ikd") # 106
        
        self.hwid = hashlib.md5(str(uuid.getnode()).encode()).hexdigest()[:12].upper() # 107
        self.prompts, self.categories_data = [], {} # 108
        self.cur_map = [] # 109
        self.cur_adm_idx = None # 110
        self.style = ttk.Style() # 111
        
        self.set_window_icon() # 112
        self.center_window(1200, 800) # 113
        
        if sys.platform == "win32": # 114
            self.register_ikd_association() # 115

        if not self.check_license(): # 116
            self.show_language_selector() # 117
        else: # 118
            self.show_main_interface() # 119

    def set_window_icon(self): # 120
        """Устанавливает иконку окна — пёрышко (n_logo.ico/icns)""" # 121
        try: # 122
            icon_ext = ".ico" if IS_WINDOWS else ".icns" # 123
            icon_path = resource_path(f"n_logo{icon_ext}") # 124
            
            if os.path.exists(icon_path): # 125
                if IS_WINDOWS: # 126
                    if IS_WINDOWS: self.root.iconbitmap(resource_path("n_logo.ico")) # 127
                else: # 128
                    # На Mac иконка устанавливается через ресурсы бандла .app # 129
                    pass # 130
            else: # 131
                print(f"Предупреждение: Файл иконки {icon_path} не найден") # 132
        except Exception as e: # 133
            print(f"Не удалось установить иконку: {e}") # 134

    def register_ikd_association(self): # 135
        """Регистрация ассоциации файлов .ikd (только Windows)""" # 136
        if not IS_WINDOWS: return # 137
        try: # 138
            appdata_path = os.environ.get('APPDATA') # 139
            icons_dir = os.path.join(appdata_path, "IKDesigns", "Icons") # 140
            os.makedirs(icons_dir, exist_ok=True) # 141
            target_icon = os.path.join(icons_dir, "ikd_file_icon.ico") # 142
            src_icon = resource_path("ikd_logo.ico") # 143
            if not os.path.exists(target_icon) and os.path.exists(src_icon): # 144
                shutil.copy2(src_icon, target_icon) # 145

            exe_path = f'"{sys.executable}"' # 146
            prog_id = "IKDesigns.NanoData" # 147

            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\.ikd") as key: # 148
                winreg.SetValue(key, "", winreg.REG_SZ, prog_id) # 149
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Classes\{prog_id}\DefaultIcon") as key: # 150
                winreg.SetValue(key, "", winreg.REG_SZ, f'"{target_icon}"') # 151
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Classes\{prog_id}\shell\open\command") as key: # 152
                winreg.SetValue(key, "", winreg.REG_SZ, f'{exe_path} "%1"') # 153

            if IS_WINDOWS: import ctypes # 154
            ctypes.windll.shell32.SHChangeNotify(0x08000000, 0x0000, None, None) # 155
        except: # 156
            pass # 157

    def center_window(self, w, h): # 156
        width = int(w * self.zoom_scale) # 157
        height = int(h * self.zoom_scale) # 158
        sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight() # 159
        x = (sw // 2) - (width // 2) # 160
        y = (sh // 2) - (height // 2) # 161
        self.root.geometry(f"{width}x{height}+{x}+{y}") # 162

    def apply_base_style(self): # 163
        s = self.zoom_scale # 164
        f_main = int(16 * s) # 165
        f_tabs = int(13 * s) # 166
        self.style.theme_use('default') # 167
        self.style.configure('TNotebook', background=BG_MAIN, borderwidth=0) # 168
        self.style.configure('TNotebook.Tab', background=BG_PANEL, foreground=TEXT_MUTED, # 169
                             padding=[int(45*s), int(18*s)], font=('Segoe UI Bold', f_tabs)) # 170
        self.style.map('TNotebook.Tab', background=[('selected', ACCENT)], foreground=[('selected', '#ffffff')]) # 171
        self.style.configure('TCombobox', font=('Segoe UI Bold', f_main)) # 172

    def apply_zoom(self, scale): # 173
        self.zoom_scale = scale # 174
        try: # 175
            current_tab = self.nb.index(self.nb.select()) # 176
        except: # 177
            current_tab = 0 # 178
        self.show_main_interface(tab_index=current_tab) # 179

    # --- ЛИЦЕНЗИЯ И ШИФРОВАНИЕ --- # 180
    def check_license(self): # 181
        if not os.path.exists(self.lic_file): return False # 182
        try: # 183
            with open(self.lic_file, "r") as f: # 184
                expected = hashlib.sha256((self.hwid + SECRET_SALT).encode()).hexdigest()[:16].upper() # 185
                return f.read().strip() == expected # 186
        except: return False # 187

    def xor_cipher(self, data): # 188
        key = SECRET_SALT # 189
        return bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(data)]) # 190

    def encrypt_data(self, data): # 191
        return base64.b64encode(self.xor_cipher(json.dumps(data, ensure_ascii=False).encode('utf-8'))) # 192

    def decrypt_data(self, encrypted): # 193
        try: # 194
            return json.loads(self.xor_cipher(base64.b64decode(encrypted)).decode('utf-8')) # 195
        except: return [] # 196

    # --- РАБОТА С БАЗОЙ --- # 197
    def get_cat_display(self, cat_ru): # 198
        val = self.categories_data.get(cat_ru, cat_ru) # 199
        return self.get_loc_text(val) if self.current_lang == "EN" else self.get_loc_text(cat_ru) # 200

    def get_loc_text(self, text): # 201
        if not text or not isinstance(text, str): return "" # 202
        text = text.strip() # 203
        start_idx = text.rfind('(') # 204
        if start_idx != -1: # 205
            end_idx = text.find(')', start_idx) # 206
            if end_idx != -1 and start_idx > 0: # 207
                ru_part = text[:start_idx].strip() # 208
                en_part = text[start_idx+1:end_idx].strip() # 209
                return en_part if self.current_lang == "EN" else ru_part # 210
        return text # 211

    def init_database(self): # 212
        for json_file in glob.glob(os.path.join(self.base_dir, "*.json")): # 213
            try: # 214
                with open(json_file, 'r', encoding='utf-8') as f: # 215
                    data = json.load(f) # 216
                counter = 1 # 217
                while os.path.exists(os.path.join(self.base_dir, f"{counter}_user_nano_prompts.ikd")): # 218
                    counter += 1 # 219
                new_path = os.path.join(self.base_dir, f"{counter}_user_nano_prompts.ikd") # 220
                with open(new_path, 'wb') as f: # 221
                    f.write(self.encrypt_data(data)) # 222
                os.remove(json_file) # 223
            except: pass # 224

        self.prompts = [] # 225
        self.categories_data = {} # 226

        all_files = [f for f in os.listdir(self.base_dir) if f.endswith(".ikd") and "nano_prompts" in f.lower()] # 227

        for f_name in all_files: # 228
            path = os.path.join(self.base_dir, f_name) # 229
            try: # 230
                with open(path, 'rb') as f: # 231
                    batch = self.decrypt_data(f.read()) # 232
                if not isinstance(batch, list): continue # 233
                for item in batch: # 234
                    if isinstance(item, dict): # 235
                        self.prompts.append(item) # 236
                        ru_cat = item.get("category", "Общее") # 237
                        self.categories_data[ru_cat] = item.get("category_en", ru_cat) # 238
            except Exception as e: # 239
                print(f"Ошибка загрузки {f_name}: {e}") # 240

        if not self.categories_data: # 241
            self.categories_data["Общее"] = "General" # 242

    # --- ГЛАВНЫЙ ИНТЕРФЕЙС --- # 243
    def show_main_interface(self, tab_index=0): # 244
        s = self.zoom_scale # 245
        for w in self.root.winfo_children(): w.destroy() # 246

        self.init_database() # 247
        self.center_window(1200, 800) # 248
        self.apply_base_style() # 249

        l = LANG_DATA[self.current_lang] # 250
        self.root.title(l["title"]) # 251

        # Header # 252
        header = tk.Frame(self.root, bg=BG_PANEL, pady=int(10*s)) # 253
        header.pack(fill="x") # 254
        tk.Label(header, text="🍌 Nano Banana Manager PRO", font=("Segoe UI Black", int(26*s)), bg=BG_PANEL, fg=ACCENT).pack(side="left", padx=int(30*s)) # 255
        tk.Button(header, text=l["about_btn"], bg="#333", fg="white", font=("Segoe UI Bold", int(10*s)), # 256
                  command=lambda: messagebox.showinfo(l["about_btn"], l["about_msg"].format(hwid=self.hwid))).pack(side="right", padx=int(10*s)) # 257
        tk.Button(header, text=l["lang_btn"], bg=ACCENT_2, fg="white", font=("Segoe UI Bold", int(10*s)), # 258
                  command=self.toggle_lang).pack(side="right", padx=int(5*s)) # 259

        zm = tk.Menubutton(header, text=l["zoom_btn"], bg="#444", fg="white", font=("Segoe UI Bold", int(10*s)), relief="flat") # 260
        zm.menu = tk.Menu(zm, tearoff=0, bg=BG_PANEL, fg="white", font=("Segoe UI", 12)) # 261
        zm["menu"] = zm.menu # 262
        for v in [1.0, 0.75, 0.5]: # 263
            zm.menu.add_command(label=f"{int(v*100)}%", command=lambda val=v: self.apply_zoom(val)) # 264
        zm.pack(side="right", padx=int(5*s)) # 265

        self.nb = ttk.Notebook(self.root) # 266
        self.nb.pack(fill="both", expand=True, padx=int(15*s), pady=int(10*s)) # 267

        t1 = tk.Frame(self.nb, bg=BG_MAIN) # 268
        t2 = tk.Frame(self.nb, bg=BG_MAIN) # 269
        t3 = tk.Frame(self.nb, bg=BG_MAIN) # 270
        t4 = tk.Frame(self.nb, bg=BG_MAIN) # 271

        self.nb.add(t1, text=l["tab_main"]) # 272
        self.nb.add(t2, text=l["tab_admin"]) # 273
        self.nb.add(t3, text=l["tab_info"]) # 274
        self.nb.add(t4, text=l["tab_help"]) # 275

        self.build_main_tab(t1, s, l) # 276
        self.build_admin_tab(t2, s, l) # 277

        # TAB 3 и 4 # 278
        for tab, content in [(t3, INFO_RU if self.current_lang == "RU" else INFO_EN), # 279
                             (t4, HELP_RU if self.current_lang == "RU" else HELP_EN)]: # 280
            clean = re.sub(r'\s*#\s*\d+$', '', content, flags=re.MULTILINE) # 281
            st = scrolledtext.ScrolledText(tab, font=("Segoe UI Semibold", int(15*s)), bg=BG_PANEL, fg=TEXT_MAIN, # 282
                                           bd=0, padx=int(45*s), pady=int(45*s), wrap="word") # 283
            st.pack(fill="both", expand=True, padx=int(15*s), pady=int(15*s)) # 284
            st.insert("1.0", clean) # 285
            st.config(state="disabled") # 286

        self.nb.select(tab_index) # 287
        self.update_list() # 288

    def build_main_tab(self, parent, s, l): # 289
        left = tk.Frame(parent, bg=BG_MAIN, width=int(350*s)) # 290
        left.pack(side="left", fill="y", padx=(0, int(20*s)), pady=int(10*s)) # 291
        left.pack_propagate(False) # 292

        tk.Label(left, text=l["nav"], font=("Segoe UI Bold", int(14*s)), bg=BG_PANEL, fg=TEXT_MAIN).pack(fill="x", pady=(0, int(10*s)), ipady=int(18*s)) # 293

        self.cat_var = tk.StringVar(value=l["all_cats"]) # 294
        self.main_cb = ttk.Combobox(left, textvariable=self.cat_var, state="readonly", font=("Segoe UI Bold", int(16*s)), justify="center") # 295
        self.main_cb.pack(fill="x", pady=(0, int(10*s)), ipady=int(15*s)) # 296
        self.main_cb.bind("<<ComboboxSelected>>", lambda e: self.update_list()) # 297

        cat_list = [l["all_cats"]] + sorted([self.get_cat_display(c) for c in self.categories_data.keys()]) # 298
        self.main_cb['values'] = cat_list # 299

        lb_f = tk.Frame(left, bg=BG_PANEL) # 300
        lb_f.pack(fill="both", expand=True) # 301
        sb = tk.Scrollbar(lb_f) # 302
        sb.pack(side="right", fill="y") # 303
        self.listbox = tk.Listbox(lb_f, bg=BG_PANEL, fg=TEXT_MAIN, bd=0, font=("Segoe UI Bold", int(16*s)), # 304
                                  selectbackground=ACCENT, highlightthickness=0, yscrollcommand=sb.set) # 305
        self.listbox.pack(side="left", fill="both", expand=True) # 306
        sb.config(command=self.listbox.yview) # 307
        self.listbox.bind("<<ListboxSelect>>", self.on_select) # 308

        right = tk.Frame(parent, bg=BG_PANEL, padx=int(30*s), pady=int(20*s)) # 309
        right.pack(side="right", fill="both", expand=True, pady=int(10*s)) # 310

        tk.Button(right, text=l["copy_btn"], bg=ACCENT, fg="white", font=("Segoe UI Bold", int(18*s)), relief="flat", pady=int(22*s), command=self.copy_p).pack(side="bottom", fill="x") # 311
        
        self.lbl_p_n = tk.Label(right, text="", font=("Segoe UI Black", int(24*s)), bg=BG_PANEL, fg=TEXT_MAIN, anchor="w", wraplength=int(750*s)) # 312
        self.lbl_p_n.pack(fill="x", pady=(0, int(5*s))) # 313

        self.lbl_main_cat = tk.Label(right, text="", font=("Segoe UI Bold", int(12*s)), bg=BG_PANEL, fg=ACCENT, anchor="w") # 314
        self.lbl_main_cat.pack(fill="x", pady=(0, int(10*s))) # 315

        tk.Label(right, text=l["main_desc_head"], font=("Segoe UI Bold", int(10*s)), bg=BG_PANEL, fg=TEXT_MUTED).pack(anchor="w") # 316
        self.txt_desc_main = tk.Text(right, bg=BG_PANEL, fg=TEXT_DESC, font=("Segoe UI", int(14*s)), bd=0, wrap="word", height=4, state="disabled") # 317
        self.txt_desc_main.pack(fill="x", pady=(int(5*s), int(15*s))) # 318

        tk.Label(right, text=l["main_prompt_head"], font=("Segoe UI Bold", int(10*s)), bg=BG_PANEL, fg=TEXT_MUTED).pack(anchor="w") # 319
        self.txt_p_main = scrolledtext.ScrolledText(right, bg="#1a1a1a", fg=TEXT_MAIN, font=("Consolas", int(15*s)), bd=0, padx=int(15*s), pady=int(15*s), state="disabled") # 320
        self.txt_p_main.pack(fill="both", expand=True) # 321

    def build_admin_tab(self, parent, s, l): # 322
        f2 = tk.Frame(parent, bg=BG_MAIN, padx=int(20*s), pady=int(10*s)) # 323
        f2.pack(fill="both", expand=True) # 324

        la = tk.Frame(f2, bg=BG_MAIN, width=int(350*s)) # 325
        la.pack(side="left", fill="y", padx=(0, int(15*s))) # 326
        la.pack_propagate(False) # 327

        cat_vals = [l["all_cats"]] + sorted([self.get_cat_display(c) for c in self.categories_data.keys()]) # 328

        self.afv = tk.StringVar(value=l["all_cats"]) # 329
        self.afc = ttk.Combobox(la, textvariable=self.afv, state="readonly", font=("Segoe UI Bold", int(16*s)), justify="center") # 330
        self.afc.pack(fill="x", pady=5, ipady=int(15*s)) # 331
        self.afc.bind("<<ComboboxSelected>>", lambda e: self.update_admin_list()) # 332
        self.afc['values'] = cat_vals # 333

        self.alb = tk.Listbox(la, bg=BG_PANEL, fg=TEXT_MAIN, bd=0, font=("Segoe UI Bold", int(16*s)), selectbackground=ACCENT) # 334
        self.alb.pack(fill="both", expand=True) # 335
        self.alb.bind("<<ListboxSelect>>", self.on_admin_select) # 336

        ra = tk.Frame(f2, bg=BG_PANEL, padx=int(25*s), pady=int(15*s)) # 337
        ra.pack(side="right", fill="both", expand=True) # 338

        tk.Button(ra, text=l["del_btn"], bg=DANGER, fg="white", font=("Segoe UI Bold", int(14*s)), pady=int(18*s), command=self.del_adm, relief="flat").pack(side="bottom", fill="x") # 339
        tk.Button(ra, text=l["save_btn"], bg=SUCCESS, fg="white", font=("Segoe UI Bold", int(14*s)), pady=int(18*s), command=self.save_adm, relief="flat").pack(side="bottom", fill="x", pady=(0, int(5*s))) # 340

        tk.Label(ra, text=l["cat_label"], bg=BG_PANEL, fg=TEXT_MAIN, font=("Segoe UI Bold", int(14*s))).pack(anchor="w") # 341

        cl = tk.Frame(ra, bg=BG_PANEL) # 342
        cl.pack(fill="x", pady=2) # 343
        self.ecc = ttk.Combobox(cl, state="readonly", font=("Segoe UI Bold", int(16*s))) # 344
        self.ecc.pack(side="left", fill="x", expand=True, ipady=int(10*s)) # 345
        self.ecc['values'] = sorted([self.get_cat_display(c) for c in self.categories_data.keys()]) # 346

        tk.Button(cl, text="+", bg=SUCCESS, fg="white", width=5, font=("Segoe UI Bold", int(13*s)), command=self.add_cat).pack(side="left", padx=5) # 347
        tk.Button(cl, text="-", bg=DANGER, fg="white", width=5, font=("Segoe UI Bold", int(13*s)), command=self.del_cat).pack(side="left") # 348

        tk.Button(ra, text=l["add_new"], bg="#444", fg="white", font=("Segoe UI Bold", int(13*s)), pady=int(12*s), command=self.clear_adm, relief="flat").pack(fill="x", pady=(int(8*s), int(10*s))) # 349

        tk.Label(ra, text=l["name_label"], bg=BG_PANEL, fg=TEXT_MAIN, font=("Segoe UI Bold", int(14*s))).pack(anchor="w") # 350
        self.a_en = tk.Entry(ra, font=("Segoe UI Bold", int(15*s)), bg=BG_MAIN, fg=TEXT_MAIN, bd=0, insertbackground="white") # 351
        self.a_en.pack(fill="x", pady=2, ipady=int(12*s)) # 352

        tk.Label(ra, text=l["desc_label"], bg=BG_PANEL, fg=TEXT_MAIN, font=("Segoe UI Bold", int(14*s))).pack(anchor="w") # 353
        self.a_rd = tk.Text(ra, height=3, font=("Segoe UI Semibold", int(14*s)), bg=BG_MAIN, fg=TEXT_MAIN, bd=0, insertbackground="white", wrap="word") # 354
        self.a_rd.pack(fill="x", pady=2) # 355

        tk.Label(ra, text=l["prompt_label"], bg=BG_PANEL, fg=TEXT_MAIN, font=("Segoe UI Bold", int(14*s))).pack(anchor="w") # 356
        self.a_tp = scrolledtext.ScrolledText(ra, height=10, font=("Consolas Bold", int(14*s)), bg=BG_MAIN, fg=TEXT_MAIN, bd=0, insertbackground="white") # 357
        self.a_tp.pack(fill="both", expand=True, pady=2) # 358

        self.update_admin_list() # 359

    # === МЕТОДЫ ДЛЯ ОСНОВНОЙ ВКЛАДКИ === # 360
    def update_list(self): # 361
        self.listbox.delete(0, tk.END) # 362
        self.cur_map = [] # 363
        sel = self.cat_var.get() # 364
        all_l = LANG_DATA[self.current_lang]["all_cats"] # 365
        for i, p in enumerate(self.prompts): # 366
            c_disp = self.get_cat_display(p.get('category', 'Общее')) # 367
            if sel == all_l or c_disp == sel: # 368
                name = p.get('name_ru', p.get('name', '')) if self.current_lang == "RU" else p.get('name_en', p.get('name', '')) # 369
                self.listbox.insert(tk.END, f" {name}") # 370
                self.cur_map.append(i) # 371
    def on_select(self, e): # 372
        if not self.listbox.curselection(): return # 373
        item = self.prompts[self.cur_map[self.listbox.curselection()[0]]] # 374

        name = item.get('name_ru', item.get('name', '')) if self.current_lang == "RU" else item.get('name_en', item.get('name', '')) # 375
        self.lbl_p_n.config(text=name) # 376

        cat_ru = item.get('category', 'Общее') # 377
        cat_disp = self.get_cat_display(cat_ru) # 378
        self.lbl_main_cat.config(text=f"{LANG_DATA[self.current_lang]['main_cat_head']} {cat_disp}") # 379

        desc = item.get('desc_ru', '') if self.current_lang == "RU" else item.get('desc_en', '') # 380
        prompt_text = item.get('prompt', '') # 381

        for w, t in [(self.txt_desc_main, desc), (self.txt_p_main, prompt_text)]: # 382
            w.config(state="normal") # 383
            w.delete("1.0", tk.END) # 384
            w.insert("1.0", t) # 385
            w.config(state="disabled") # 386

    def copy_p(self): # 387
        c = self.txt_p_main.get("1.0", tk.END).strip() # 388
        if c: # 389
            self.root.clipboard_clear() # 390
            self.root.clipboard_append(c) # 391
            messagebox.showinfo("OK", LANG_DATA[self.current_lang]["copy_ok"]) # 392

    def toggle_lang(self): # 393
        self.current_lang = "EN" if self.current_lang == "RU" else "RU" # 394
        self.show_main_interface() # 395

    # === УПРАВЛЕНИЕ === # 396
    def update_admin_list(self): # 397
        self.alb.delete(0, tk.END) # 398
        self.adm_map = [] # 399
        sel = self.afv.get() # 400
        all_l = LANG_DATA[self.current_lang]["all_cats"] # 401
        for i, p in enumerate(self.prompts): # 402
            c_disp = self.get_cat_display(p.get('category', 'Общее')) # 403
            if sel == all_l or c_disp == sel: # 404
                name = p.get('name_ru', p.get('name', '')) if self.current_lang == "RU" else p.get('name_en', p.get('name', '')) # 405
                self.alb.insert(tk.END, f" {name}") # 406
                self.adm_map.append(i) # 407

    def on_admin_select(self, e): # 408
        if not self.alb.curselection(): return # 409
        self.cur_adm_idx = self.adm_map[self.alb.curselection()[0]] # 410
        it = self.prompts[self.cur_adm_idx] # 411
        self.ecc.set(self.get_cat_display(it.get('category', 'Общее'))) # 412
        
        self.a_en.delete(0, tk.END) # 413
        name = it.get('name_ru', it.get('name', '')) if self.current_lang == "RU" else it.get('name_en', it.get('name', '')) # 414
        self.a_en.insert(0, name) # 415
        
        self.a_tp.delete("1.0", tk.END) # 416
        self.a_tp.insert("1.0", it.get('prompt', '')) # 417
        
        self.a_rd.delete("1.0", tk.END) # 418
        desc = it.get('desc_ru', '') if self.current_lang == "RU" else it.get('desc_en', it.get('desc_ru', '')) # 419
        self.a_rd.insert("1.0", desc) # 420

    def save_adm(self): # 421
        c_disp, n = self.ecc.get(), self.a_en.get().strip() # 422
        if not (c_disp and n): return # 423
        ru = next((r for r, e in self.categories_data.items() if e == c_disp or r == c_disp), c_disp) # 424
        new = {"name": n, "category": ru, "category_en": self.categories_data.get(ru, ru), # 425
               "prompt": self.a_tp.get("1.0", tk.END).strip(), "desc_ru": self.a_rd.get("1.0", tk.END).strip()} # 426
        user_list = [] # 427
        if os.path.exists(self.user_data_file): # 428
            try: # 429
                with open(self.user_data_file, 'rb') as f: user_list = self.decrypt_data(f.read()) # 430
            except: pass # 431
        if self.cur_adm_idx is not None: # 432
            old_n = self.prompts[self.cur_adm_idx].get('name', '') # 433
            user_list = [p for p in user_list if p.get('name', '') != old_n] # 434
        user_list.append(new) # 435
        with open(self.user_data_file, 'wb') as f: f.write(self.encrypt_data(user_list)) # 436
        self.show_main_interface(tab_index=1) # 437

    def del_adm(self): # 438
        l = LANG_DATA[self.current_lang] # 439
        if self.cur_adm_idx is None or not messagebox.askyesno(l["confirm_del"], l["ask_del"]): return # 440
        n = self.prompts[self.cur_adm_idx].get('name', '') # 441
        try: # 442
            with open(self.user_data_file, 'rb') as f: user_list = self.decrypt_data(f.read()) # 443
            user_list = [p for p in user_list if p.get('name', '') != n] # 444
            with open(self.user_data_file, 'wb') as f: f.write(self.encrypt_data(user_list)) # 445
            self.show_main_interface(tab_index=1) # 446
        except: pass # 447

    def add_cat(self): # 448
        n = simpledialog.askstring("RU", "Название (RU):") # 449
        if n and n not in self.categories_data: # 450
            en = simpledialog.askstring("EN", "Name (EN):") # 451
            self.categories_data[n] = en if en else n # 452
            cat_list = [LANG_DATA[self.current_lang]["all_cats"]] + sorted([self.get_cat_display(c) for c in self.categories_data.keys()]) # 453
            self.main_cb['values'] = cat_list # 454
            self.afc['values'] = cat_list # 455
            self.ecc['values'] = sorted([self.get_cat_display(c) for c in self.categories_data.keys()]) # 456
            self.ecc.set(self.get_cat_display(n)) # 457

    def del_cat(self): # 458
        l = LANG_DATA[self.current_lang] # 459
        cd = self.ecc.get() # 460
        if cd and messagebox.askyesno(l["confirm_del"], l["ask_del"]): # 461
            rc = next((r for r, e in self.categories_data.items() if e == cd or r == cd), cd) # 462
            self.categories_data.pop(rc, None) # 463
            self.show_main_interface(tab_index=1) # 464

    def clear_adm(self): # 465
        self.cur_adm_idx = None # 466
        self.a_en.delete(0, tk.END) # 467
        self.a_tp.delete("1.0", tk.END) # 468
        self.a_rd.delete("1.0", tk.END) # 469

    # --- Окно активации --- # 470
    def show_language_selector(self): # 471
        for w in self.root.winfo_children(): w.destroy() # 472
        self.center_window(1200, 800) # 473
        c = tk.Frame(self.root, bg=BG_MAIN); c.place(relx=0.5, rely=0.5, anchor="center") # 474
        tk.Label(c, text="CHOOSE LANGUAGE / ВЫБЕРИТЕ ЯЗЫК", font=("Segoe UI Bold", 18), bg=BG_MAIN, fg=TEXT_MAIN).pack(pady=20) # 475
        btn_f = tk.Frame(c, bg=BG_MAIN); btn_f.pack() # 476
        tk.Button(btn_f, text="ENGLISH", bg=ACCENT, fg="white", font=("Segoe UI Bold", 14), width=15, pady=10, # 477
                  command=lambda: self.set_lang_and_auth("EN")).pack(side="left", padx=10) # 478
        tk.Button(btn_f, text="РУССКИЙ", bg=ACCENT_2, fg="white", font=("Segoe UI Bold", 14), width=15, pady=10, # 479
                  command=lambda: self.set_lang_and_auth("RU")).pack(side="left", padx=10) # 480

    def set_lang_and_auth(self, lang): # 481
        self.current_lang = lang # 482
        self.show_auth_window() # 483

    def show_auth_window(self): # 484
        for widget in self.root.winfo_children(): widget.destroy() # 485
        txt = { # 486
            "RU": {"head": "🍌 Nano Banana PRO", "id": f"ID устройства: {self.hwid}", "copy": "📋 Копировать ID", # 487
                   "get_key": "🌐 ПОЛУЧИТЬ КЛЮЧ АКТИВАЦИИ", "act": "АКТИВИРОВАТЬ", "msg": "ID скопирован!", # 488
                   "err": "Ошибка активации", "back": "↩ НАЗАД", "paste": "📋 ВСТАВИТЬ КЛЮЧ"}, # 489
            "EN": {"head": "🍌 Nano Banana PRO", "id": f"Device ID: {self.hwid}", "copy": "📋 Copy ID", # 490
                   "get_key": "🌐 GET ACTIVATION KEY", "act": "ACTIVATE", "msg": "ID copied!", # 491
                   "err": "Activation Error", "back": "↩ BACK", "paste": "📋 PASTE KEY"} # 492
        }[self.current_lang] # 493

        c = tk.Frame(self.root, bg=BG_MAIN); c.place(relx=0.5, rely=0.5, anchor="center") # 494
        tk.Button(c, text=txt["back"], bg=BG_PANEL, fg=TEXT_MUTED, font=("Segoe UI Bold", 10), bd=0, padx=10, pady=5, # 495
                  command=self.show_language_selector).pack(anchor="nw", pady=(0, 20)) # 496
        tk.Label(c, text=txt["head"], font=("Segoe UI Black", 42), bg=BG_MAIN, fg=ACCENT).pack() # 497
        idf = tk.Frame(c, bg=BG_MAIN, pady=15); idf.pack() # 498
        tk.Label(idf, text=txt["id"], bg=BG_MAIN, fg=TEXT_MUTED, font=("Consolas", 14)).pack(side="left", padx=15) # 499
        tk.Button(idf, text=txt["copy"], bg="#333", fg="white", font=("Segoe UI Bold", 10), # 500
                  command=lambda: (self.root.clipboard_clear(), self.root.clipboard_append(self.hwid), messagebox.showinfo("OK", txt["msg"]))).pack(side="left") # 501
        tk.Button(c, text=txt["get_key"], bg="#333", fg="white", font=("Segoe UI Bold", 13), # 502
                  command=lambda: webbrowser.open(f"https://koresh71.github.io/activation/?hwid={self.hwid}")).pack(pady=15) # 503
        self.ki = tk.Entry(c, font=("Consolas", 22), justify="center", bg=BG_PANEL, fg="white", width=25, insertbackground="white") # 504
        self.ki.pack(pady=10, ipady=10) # 505
        tk.Button(c, text=txt["paste"], bg="#475569", fg="white", font=("Segoe UI Bold", 10), # 506
                  command=lambda: (self.ki.delete(0, tk.END), self.ki.insert(0, self.root.clipboard_get()))).pack(pady=5) # 507
        tk.Button(c, text=txt["act"], bg=ACCENT, fg="white", font=("Segoe UI Bold", 16), padx=50, pady=20, # 508
                  command=lambda: self.activate_now(self.ki.get().strip().upper(), txt["err"])).pack(pady=25) # 509

    def activate_now(self, k, err_msg): # 510
        expected = hashlib.sha256((self.hwid + SECRET_SALT).encode()).hexdigest()[:16].upper() # 511
        if k == expected: # 512
            with open(self.lic_file, "w") as f: f.write(k) # 513
            self.show_main_interface() # 514
        else: # 515
            messagebox.showerror("X", err_msg) # 516

# --- ТОЧКА ВХОДА --- # 517
if __name__ == "__main__": # 518
    root = tk.Tk() # 519
    app = NanoBananaManager(root) # 520
    root.mainloop() # 521