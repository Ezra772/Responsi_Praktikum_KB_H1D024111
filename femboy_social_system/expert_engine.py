QUESTIONS = {

    'q1':  "Apakah kamu sering menonton anime atau mengikuti budaya pop Jepang?",
    'q2':  "Apakah kamu mengikuti konten K-pop atau budaya Korea?",
    'q3':  "Apakah kamu sering terpapar konten tentang keberagaman gender di media sosial?",
    'q4':  "Apakah kamu pernah menonton film atau serial yang menampilkan karakter dengan ekspresi gender non-konformis?",
    'q5':  "Apakah kamu aktif di komunitas gaming, cosplay, atau fandom online?",
    'q6':  "Apakah kamu percaya bahwa penampilan seseorang adalah hak dan urusan pribadi mereka?",
    'q7':  "Apakah kamu percaya norma gender sebaiknya bersifat fleksibel, bukan kaku?",
    'q8':  "Apakah keyakinan agama atau kepercayaanmu sangat memengaruhi pandanganmu tentang ekspresi gender?",
    'q9':  "Apakah menurutmu kebebasan berekspresi lebih penting daripada norma sosial yang berlaku?",
    'q10': "Apakah kamu menghargai individualitas dan keunikan setiap orang, termasuk cara mereka berpenampilan?",
    'q11': "Apakah lingkungan keluargamu cenderung konservatif atau tradisional dalam memandang peran gender?",
    'q12': "Apakah teman-teman dekatmu umumnya terbuka dan menerima keberagaman?",
    'q13': "Apakah komunitas di lingkungan tempat tinggalmu menerima perbedaan gaya hidup dan penampilan?",
    'q14': "Apakah lingkungan sekolah, kampus, atau tempat kerjamu mendukung sikap inklusif?",
    'q15': "Apakah kamu tinggal atau besar di lingkungan perkotaan yang relatif terbuka?",
    'q16': "Apakah kamu pernah berinteraksi langsung dengan seseorang yang berpenampilan femboy?",
    'q17': "Apakah kamu memiliki teman atau kenalan yang mengekspresikan diri secara feminin meskipun berjenis kelamin laki-laki?",
    'q18': "Apakah pengalaman pribadimu dengan individu berpenampilan femboy bersifat positif?",
    'q19': "Apakah kamu pernah menghadiri acara atau bergabung komunitas yang inklusif terhadap ekspresi gender?",
    'q20': "Apakah kamu pernah menyaksikan seseorang diperlakukan tidak adil karena penampilannya?",
    'q21': "Apakah kamu mampu memahami dan berempati terhadap perasaan orang yang berbeda darimu?",
    'q22': "Apakah kamu merasa nyaman berada di sekitar orang yang penampilannya berbeda dari norma umum?",
    'q23': "Apakah kamu cenderung menilai seseorang dari karakter dan perilakunya, bukan dari penampilannya?",
    'q24': "Apakah kamu merasa tidak nyaman atau terganggu melihat laki-laki berpenampilan feminin di tempat umum?",
    'q25': "Apakah kamu pernah secara aktif mengkritik atau mempermasalahkan penampilan orang lain?",
    'q26': "Apakah kamu akan membela seseorang yang diejek atau di-bully karena penampilannya?",
    'q27': "Apakah kamu akan menegur orang yang melakukan intimidasi terhadap individu berpenampilan femboy?",
    'q28': "Apakah kamu lebih memilih diam dan tidak ikut campur ketika melihat situasi diskriminasi?",
    'q29': "Apakah kamu bersedia mengedukasi orang lain tentang pentingnya menghormati perbedaan ekspresi gender?",
    'q30': "Apakah kamu akan secara terbuka mendukung hak kebebasan ekspresi gender di media sosial atau ruang publik?",
}

QUESTION_CATEGORIES = [
    {'name': 'Media & Paparan Budaya',  'icon': '🎬', 'questions': ['q1','q2','q3','q4','q5']},
    {'name': 'Nilai & Keyakinan',      'icon': '💎', 'questions': ['q6','q7','q8','q9','q10']},
    {'name': 'Lingkungan Sosial',        'icon': '🏘️', 'questions': ['q11','q12','q13','q14','q15']},
    {'name': 'Pengalaman Pribadi',      'icon': '🤝', 'questions': ['q16','q17','q18','q19','q20']},
    {'name': 'Empati & Pola Pikir',      'icon': '🧠', 'questions': ['q21','q22','q23','q24','q25']},
    {'name': 'Tindakan & Perilaku',   'icon': '⚡', 'questions': ['q26','q27','q28','q29','q30']},
]

PROFILES = {
    'menolak_keras': {
        'label':     '🔴 Menolak Keras',
        'color':     '#ff1744',
        'deskripsi': 'Kamu cenderung menolak secara aktif dan terbuka terhadap keberadaan individu femboy. '
                     'Sikap ini biasanya dipengaruhi kuat oleh latar belakang budaya konservatif, keyakinan '
                     'bahwa norma gender bersifat mutlak, dan minimnya interaksi langsung dengan individu beragam.',
        'saran':     'Cobalah membuka ruang dialog dengan perspektif yang berbeda. Eksplorasi budaya populer '
                     'dan interaksi langsung dengan komunitas beragam bisa membantu memperluas pandangan.',
    },
    'menolak_pasif': {
        'label':     '🟠 Menolak Pasif',
        'color':     '#ff6d00',
        'deskripsi': 'Kamu tidak menyetujui fenomena femboy namun tidak bersikap konfrontatif. Ada rasa '
                     'ketidaknyamanan, tetapi kamu memilih untuk tidak mengekspresikannya secara langsung.',
        'saran':     'Interaksi langsung dan natural dengan komunitas beragam sering kali efektif menggeser '
                     'ketidaknyamanan ini secara bertahap.',
    },
    'netral': {
        'label':     '🟡 Netral',
        'color':     '#ffd600',
        'deskripsi': 'Kamu tidak memiliki opini kuat ke arah manapun mengenai fenomena femboy. Sikap ini '
                     'bisa merupakan bentuk ketidaktahuan, ketidakpedulian, atau kebijaksanaan pragmatis.',
        'saran':     'Netralitas adalah titik awal yang baik. Memperluas wawasan melalui media dan '
                     'pengalaman langsung bisa membentuk perspektif yang lebih matang.',
    },
    'toleran': {
        'label':     '🟢 Toleran',
        'color':     '#00e676',
        'deskripsi': 'Kamu menerima keberadaan individu femboy tanpa perlu mendukung secara aktif. '
                     'Prinsip "hidup dan biarkan hidup" mendominasi sikapmu.',
        'saran':     'Toleransi adalah fondasi yang kuat. Langkah bermakna selanjutnya adalah bersuara '
                     'ketika menyaksikan perlakuan tidak adil.',
    },
    'mendukung': {
        'label':     '🔵 Mendukung',
        'color':     '#40c4ff',
        'deskripsi': 'Kamu secara aktif mendukung kebebasan ekspresi dan hak individu untuk tampil sesuai '
                     'identitasnya. Sikapmu yang terbuka, empatik, dan inklusif mencerminkan pemahaman '
                     'mendalam tentang keberagaman manusia.',
        'saran':     'Terus pertahankan sikap ini dan jadilah ruang aman bagi orang-orang di sekitarmu.',
    },
}


RULES = [
    ({'q11': True,  'q24': True,  'q7': False, 'q25': True},'menolak_keras'),
    ({'q8': True,   'q24': True,  'q26': False,'q25': True},'menolak_keras'),
    ({'q11': True,  'q24': True,  'q7': False, 'q26': False},'menolak_keras'),
    ({'q25': True,  'q24': True,  'q28': True, 'q8': True},'menolak_keras'),
    ({'q11': True,  'q7': False,  'q25': True, 'q10': False},'menolak_keras'),
    ({'q3': False,  'q11': True,  'q24': True, 'q25': True},'menolak_keras'),
    ({'q26': False, 'q29': False, 'q25': True, 'q24': True},'menolak_keras'),

    ({'q24': True,  'q25': False, 'q26': False},'menolak_pasif'),
    ({'q11': True,  'q24': True,  'q25': False, 'q28': True},'menolak_pasif'),
    ({'q8': True,   'q24': True,  'q25': False, 'q28': True},'menolak_pasif'),
    ({'q7': False,  'q28': True,  'q6': False,  'q25': False},'menolak_pasif'),
    ({'q16': False, 'q24': True,  'q26': False, 'q25': False},'menolak_pasif'),
    ({'q11': True,  'q12': False, 'q24': True,  'q25': False},'menolak_pasif'),

    ({'q24': False, 'q6': False,  'q7': False,  'q26': False},'netral'),
    ({'q3': False,  'q16': False, 'q24': False, 'q28': True},'netral'),
    ({'q16': False, 'q24': False, 'q9': False,  'q30': False},'netral'),
    ({'q1': False,  'q17': False, 'q28': True,  'q24': False},'netral'),
    ({'q15': False, 'q13': False, 'q24': False, 'q26': False},'netral'),

    ({'q24': False, 'q6': True,   'q7': True,   'q30': False},'toleran'),
    ({'q16': True,  'q24': False, 'q10': True,  'q30': False},'toleran'),
    ({'q12': True,  'q24': False, 'q6': True,   'q29': False},'toleran'),
    ({'q21': True,  'q24': False, 'q6': True,   'q27': False},'toleran'),
    ({'q3': True,   'q24': False, 'q23': True,  'q27': False},'toleran'),
    ({'q18': True,  'q24': False, 'q10': True,  'q30': False},'toleran'),

    ({'q26': True,  'q7': True,   'q9': True,   'q29': True},'mendukung'),
    ({'q26': True,  'q27': True,  'q30': True,  'q21': True},'mendukung'),
    ({'q16': True,  'q26': True,  'q7': True,   'q6': True},'mendukung'),
    ({'q1': True,   'q26': True,  'q29': True,  'q30': True},'mendukung'),
    ({'q21': True,  'q22': True,  'q26': True,  'q27': True},'mendukung'),
    ({'q18': True,  'q17': True,  'q26': True,  'q30': True},'mendukung'),
    ({'q10': True,  'q9': True,   'q26': True,  'q28': False},'mendukung'),
    ({'q14': True,  'q21': True,  'q26': True,  'q29': True},'mendukung'),
]


def analyze_expert(answers: dict) -> dict:
    matched_rules = []

    for rule_conditions, conclusion in RULES:
        if _match(answers, rule_conditions):
            matched_rules.append((rule_conditions, conclusion))

    if not matched_rules:
        conclusion = _fallback(answers)
    else:
        from collections import Counter
        count = Counter(c for _, c in matched_rules)
        top   = count.most_common(1)[0][0]

        candidates = [r for r in matched_rules if r[1] == top]
        best_rule  = max(candidates, key=lambda r: len(r[0]))
        conclusion = best_rule[1]

    profile       = PROFILES[conclusion]
    fired_rules   = _explain(matched_rules, answers)

    return {
        'profil'     : profile,
        'konklusi'   : conclusion,
        'fired_rules': fired_rules,
        'total_fired': len(matched_rules),
    }


def _match(answers: dict, conditions: dict) -> bool:
    return all(answers.get(k) == v for k, v in conditions.items())


def _fallback(answers: dict) -> str:
    positif = sum([
        answers.get('q1', False),  answers.get('q2', False),
        answers.get('q3', False),  answers.get('q4', False),
        answers.get('q5', False),  answers.get('q6', False),
        answers.get('q7', False),  answers.get('q9', False),
        answers.get('q10', False), answers.get('q12', False),
        answers.get('q13', False), answers.get('q14', False),
        answers.get('q15', False), answers.get('q16', False),
        answers.get('q17', False), answers.get('q18', False),
        answers.get('q19', False), answers.get('q20', False),
        answers.get('q21', False), answers.get('q22', False),
        answers.get('q23', False), answers.get('q26', False),
        answers.get('q27', False), answers.get('q29', False),
        answers.get('q30', False),
    ])
    negatif = sum([
        answers.get('q8', False),  answers.get('q11', False),
        answers.get('q24', False), answers.get('q25', False),
        answers.get('q28', False),
    ])
    skor = positif - negatif
    if skor >= 16:  return 'mendukung'
    if skor >= 10:  return 'toleran'
    if skor >= 4:   return 'netral'
    if skor >= 0:   return 'menolak_pasif'
    return 'menolak_keras'


def _explain(matched_rules: list, answers: dict) -> list:
    result = []
    seen   = set()
    for conditions, conclusion in matched_rules:
        key = (frozenset(conditions.items()), conclusion)
        if key in seen:
            continue
        seen.add(key)
        cond_text = " DAN ".join(
            f"{'✅' if v else '❌'} {QUESTIONS[k][:50]}..."
            for k, v in conditions.items()
        )
        result.append({
            'kondisi'  : cond_text,
            'konklusi' : PROFILES[conclusion]['label'],
            'color'    : PROFILES[conclusion]['color'],
        })
    return result


def get_questions() -> dict:
    return QUESTIONS

def get_categories() -> list:
    return QUESTION_CATEGORIES