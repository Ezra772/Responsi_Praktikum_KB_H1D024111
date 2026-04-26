import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64

def analyze_fuzzy(data):
    x = np.arange(0, 10.1, 0.1)

    eksposur      = ctrl.Antecedent(x, 'eksposur_media')
    budaya        = ctrl.Antecedent(x, 'latar_budaya')
    lingkungan    = ctrl.Antecedent(x, 'lingkungan_sosial')
    empati        = ctrl.Antecedent(x, 'tingkat_empati')
    penerimaan    = ctrl.Consequent(x, 'tingkat_penerimaan')

    for var in [eksposur, budaya, lingkungan, empati]:
        var['rendah']  = fuzz.trimf(var.universe, [0, 0, 5])
        var['sedang']  = fuzz.trimf(var.universe, [2, 5, 8])
        var['tinggi']  = fuzz.trimf(var.universe, [5, 10, 10])

    penerimaan['rendah']  = fuzz.trimf(penerimaan.universe, [0, 0, 4])
    penerimaan['sedang']  = fuzz.trimf(penerimaan.universe, [2, 5, 8])
    penerimaan['tinggi']  = fuzz.trimf(penerimaan.universe, [6, 10, 10])

    rules = [
        ctrl.Rule(eksposur['tinggi'] & budaya['tinggi'],              penerimaan['tinggi']),
        ctrl.Rule(eksposur['tinggi'] & empati['tinggi'],              penerimaan['tinggi']),
        ctrl.Rule(lingkungan['tinggi'] & empati['tinggi'],            penerimaan['tinggi']),
        ctrl.Rule(budaya['tinggi'] & lingkungan['tinggi'],            penerimaan['tinggi']),
        ctrl.Rule(budaya['sedang'] & empati['tinggi'],                penerimaan['sedang']),
        ctrl.Rule(eksposur['sedang'] & lingkungan['sedang'],          penerimaan['sedang']),
        ctrl.Rule(budaya['sedang'] & lingkungan['sedang'],            penerimaan['sedang']),
        ctrl.Rule(empati['sedang'] & eksposur['sedang'],              penerimaan['sedang']),
        ctrl.Rule(budaya['rendah'] & lingkungan['rendah'],            penerimaan['rendah']),
        ctrl.Rule(eksposur['rendah'] & budaya['rendah'],              penerimaan['rendah']),
        ctrl.Rule(eksposur['rendah'] & empati['rendah'],              penerimaan['rendah']),
        ctrl.Rule(lingkungan['rendah'] & empati['rendah'],            penerimaan['rendah']),
        ctrl.Rule(budaya['tinggi'] & empati['rendah'],                penerimaan['sedang']),
        ctrl.Rule(eksposur['tinggi'] & budaya['rendah'],              penerimaan['sedang']),
        ctrl.Rule(budaya['rendah'] & empati['tinggi'],                penerimaan['sedang']),
        ctrl.Rule(lingkungan['tinggi'] & budaya['rendah'],            penerimaan['sedang']),
        ctrl.Rule(eksposur['rendah'] & lingkungan['tinggi'] & empati['tinggi'], penerimaan['sedang']),
        ctrl.Rule(budaya['sedang'] & lingkungan['tinggi'] & empati['tinggi'],   penerimaan['tinggi']),
        ctrl.Rule(eksposur['rendah'] & budaya['rendah'] & empati['rendah'],     penerimaan['rendah']),
        ctrl.Rule(eksposur['tinggi'] & budaya['tinggi'] & empati['tinggi'],     penerimaan['tinggi']),
        ctrl.Rule(eksposur['sedang'] | budaya['sedang'] | lingkungan['sedang'] | empati['sedang'], penerimaan['sedang']),
        ctrl.Rule(eksposur['tinggi'] | budaya['tinggi'] | lingkungan['tinggi'] | empati['tinggi'], penerimaan['tinggi']),
        ctrl.Rule(eksposur['rendah'] | budaya['rendah'] | lingkungan['rendah'] | empati['rendah'], penerimaan['rendah']),
    ]

    system = ctrl.ControlSystem(rules)
    sim    = ctrl.ControlSystemSimulation(system)

    sim.input['eksposur_media']    = data['eksposur_media']
    sim.input['latar_budaya']      = data['latar_budaya']
    sim.input['lingkungan_sosial'] = data['lingkungan_sosial']
    sim.input['tingkat_empati']    = data['tingkat_empati']

    try:
        sim.compute()
        output_val = sim.output['tingkat_penerimaan']
    except (KeyError, Exception):
        vals = list(data.values())
        output_val = float(np.mean(vals))

    if output_val < 3.5:
        label       = "Penolakan"
        color       = "#e74c3c"
        deskripsi   = "Masyarakat cenderung menolak atau tidak menerima individu berkarakter femboy di lingkungan ini."
    elif output_val < 6.5:
        label       = "Netral / Toleran"
        color       = "#f39c12"
        deskripsi   = "Masyarakat bersikap netral atau toleran, menerima tanpa dukungan aktif."
    else:
        label       = "Penerimaan"
        color       = "#2ecc71"
        deskripsi   = "Masyarakat cenderung menerima dan mendukung kebebasan ekspresi individu femboy."

    chart_b64 = _generate_chart(penerimaan, output_val)

    return {
        'nilai'      : round(output_val, 2),
        'label'      : label,
        'color'      : color,
        'deskripsi'  : deskripsi,
        'chart'      : chart_b64,
    }


def _generate_chart(penerimaan_var, output_val):
    fig, ax = plt.subplots(figsize=(7, 3.2), facecolor='#0f0f0f')
    ax.set_facecolor('#1a1a1a')

    colors = {'rendah': '#e74c3c', 'sedang': '#f39c12', 'tinggi': '#2ecc71'}
    x = penerimaan_var.universe

    for label, color in colors.items():
        ax.plot(x, fuzz.trimf(x, [0,0,4] if label=='rendah' else ([2,5,8] if label=='sedang' else [6,10,10])),
                color=color, lw=2, label=label.capitalize())

    ax.axvline(x=output_val, color='white', lw=1.5, linestyle='--', alpha=0.8, label=f'Output: {output_val:.2f}')
    ax.set_xlabel('Tingkat Penerimaan', color='#aaa', fontsize=9)
    ax.set_ylabel('Derajat Keanggotaan', color='#aaa', fontsize=9)
    ax.tick_params(colors='#777')
    for spine in ax.spines.values():
        spine.set_edgecolor('#333')
    ax.legend(facecolor='#1a1a1a', edgecolor='#333', labelcolor='white', fontsize=8)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=130, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')