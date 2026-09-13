"""
===============================================================================
O ATEMPORAL: MODELAGEM COMPUTACIONAL DA 20ª FORMA ANALÍTICA
Princípio da Proporcionalidade Inversa (Antônio Marcos, 2026 - CC BY 4.0)

Mapeamento Telemétrico: Escala Física Real (SI) e Métrica Relativa Normalizada.
Inclui renderização gráfica automática via Matplotlib.
===============================================================================
"""

import math
import sys

# 🛠️ Tenta importar a biblioteca de gráficos. Se o usuário não tiver instalada, o código avisa sem quebrar.
try:
    import matplotlib.pyplot as plt
    import numpy as np
    GRAFICOS_DISPONIVEIS = True
except ImportError:
    GRAFICOS_DISPONIVEIS = False

def calcular_telemetria_real_si(M_campo, m_fluxo, z, chi, theta_graus):
    """Calcula o raio telemétrico real em metros (Sistema Internacional)."""
    G = 6.67430e-11  
    c = 299792458    
    theta = math.radians(theta_graus)
    
    R_s = (2 * G * M_campo) / (c**2)
    raiz_base = R_s * math.sqrt(m_fluxo / M_campo)
    
    fator_spin = 2 / (1 + math.sqrt(1 - chi**2))
    fator_redshift = 1 - (1 / (z + 1)**2)
    fator_inclinacao = math.sqrt((G * M_campo) / (c**2)) * math.sin(theta)
    
    termo_esquerdo = (raiz_base * fator_spin) / fator_redshift
    termo_direito = fator_inclinacao ** 2
    
    return termo_esquerdo + termo_direito

def calcular_raio_normalizado_rs(z, chi, theta_graus):
    """Calcula a distância telemétrica adimensional em múltiplos puros de r_s."""
    theta = math.radians(theta_graus)
    
    base_relativa = 1.0
    fator_spin = 2 / (1 + math.sqrt(1 - chi**2))
    fator_redshift = 1 - (1 / (z + 1)**2)
    fator_inclinacao = 0.5 * math.sin(theta)  
    
    termo_esquerdo = (base_relativa * fator_spin) / fator_redshift
    termo_direito = fator_inclinacao ** 2
    
    return termo_esquerdo + termo_direito

def gerar_janela_grafica():
    """Gera e exibe a curva contínua do comportamento da 20ª forma."""
    if not GRAFICOS_DISPONIVEIS:
        print("\n[AVISO VISUAL] Para abrir a janela gráfica automática, instale as bibliotecas digitando:")
        print("👉 pip install matplotlib numpy")
        return

    # Gera 200 pontos de redshift de forma contínua entre z=0.05 e z=3.0
    z_escala = np.linspace(0.05, 3.0, 200)
    raios_calculados = []
    
    for z_ponto in z_escala:
        r_rs = calcular_raio_normalizado_rs(z_ponto, chi=0.90, theta_graus=30)
        raios_calculados.append(r_rs)
        
    # Pontos discretos do terminal para marcar no gráfico
    z_pontos_reais = [0.10, 0.41, 1.00, 2.50]
    r_pontos_reais = [calcular_raio_normalizado_rs(p, 0.90, 30) for p in z_pontos_reais]

    # Configuração da Janela de Plotagem
    plt.figure(figsize=(8, 5))
    plt.plot(z_escala, raios_calculados, color='#00cbd6', linewidth=2.5, label='Curva de Telemetria (Giro e Inclinação)')
    plt.scatter(z_pontos_reais, r_pontos_reais, color='red', s=60, zorder=5, label='Camadas Mapeadas (Terminal)')
    plt.axhline(y=1.0, color='r', linestyle='--', alpha=0.5, label='Horizonte Estático de Base (1.0 rs)')
    
    plt.title('O Atemporal - Mapeamento da Ergoregião (20ª Forma)', fontsize=12, weight='bold')
    plt.xlabel('Desvio para o Vermelho Gravitacional (Redshift z)')
    plt.ylabel('Raio Telemétrico Relativo (R / rs)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    
    print("\n[VISUAL] Abrindo a janela com o gráfico da sua equação na tela...")
    plt.show()

if __name__ == "__main__":
    M_SOLAR = 1.989e30
    massa_m87 = M_SOLAR * 6500000000
    
    print("=" * 75)
    print("   LABORATÓRIO COMPUTACIONAL O ATEMPORAL - SIMULAÇÃO DA 20ª FORMA")
    print("=" * 75)
    print("MODO IV: Telemetria Física Real (Objeto de Estudo: Monstro Supermassivo M87*)")
    print("-" * 75)
    
    r_estatico = calcular_telemetria_real_si(massa_m87, massa_m87, 100000.0, 0.0, 0)
    r_kerr = calcular_telemetria_real_si(massa_m87, massa_m87, 100000.0, 0.90, 17)
    
    print(f"-> M87* Schwarzschild Estático (theta=0°, chi=0.0): {r_estatico / 1e12:.3f} Bilhões de km")
    print(f"-> M87* Kerr Dinâmico Real    (theta=17°, chi=0.90): {r_kerr / 1e12:.3f} Bilhões de km")
    
    print("\n" + "-" * 75)
    print("MODO B: Mapeamento de Camadas do Disco em Unidades Relativas (r_s)")
    print("-" * 75)
    
    camadas = [("Disco Externo", 0.10), ("Disco Intermediário", 0.41), 
               ("Limiar Dinâmico", 1.00), ("Borda Interna Extrema", 2.50)]
    
    for nome, z_obs in camadas:
        r_rs = calcular_raio_normalizado_rs(z_obs, 0.90, 30)
        print(f"-> {nome:<25} (z = {z_obs:.2f}) -> R ≈ {r_rs:.2f} r_s")
        
    print("=" * 75)
    
    # Executa a renderização gráfica
    gerar_janela_grafica()
