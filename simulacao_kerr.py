"""
===============================================================================
O ATEMPORAL: MODELAGEM COMPUTACIONAL DA 20ª FORMA ANALÍTICA
Princípio da Proporcionalidade Inversa (Antônio Marcos, 2026 - CC BY 4.0)

Mapeamento Telemétrico: Escala Física Real (SI) e Métrica Relativa Normalizada.
===============================================================================
"""

import math

def calcular_telemetria_real_si(M_campo, m_fluxo, z, chi, theta_graus):
    """Calcula o raio telemétrico real em metros (Sistema Internacional)."""
    G = 6.67430e-11  # Constante Gravitacional de Newton
    c = 299792458    # Velocidade da Luz
    theta = math.radians(theta_graus)
    
    # 1. Raio Base Unificado (Consistência m ≡ M)
    R_s = (2 * G * M_campo) / (c**2)
    raiz_base = R_s * math.sqrt(m_fluxo / M_campo)
    
    # 2. Correções da 20ª Forma
    fator_spin = 2 / (1 + math.sqrt(1 - chi**2))
    fator_redshift = 1 - (1 / (z + 1)**2)
    fator_inclinacao = math.sqrt((G * M_campo) / (c**2)) * math.sin(theta)
    
    # Montagem Polinomial
    termo_esquerdo = (raiz_base * fator_spin) / fator_redshift
    termo_direito = fator_inclinacao ** 2
    
    return termo_esquerdo + termo_direito

def calcular_raio_normalizado_rs(z, chi, theta_graus):
    """Calcula a distância telemétrica adimensional em múltiplos puros de r_s."""
    theta = math.radians(theta_graus)
    
    base_relativa = 1.0
    fator_spin = 2 / (1 + math.sqrt(1 - chi**2))
    fator_redshift = 1 - (1 / (z + 1)**2)
    fator_inclinacao = 0.5 * math.sin(theta)  # Redução geométrica proporcional
    
    termo_esquerdo = (base_relativa * fator_spin) / fator_redshift
    termo_direito = fator_inclinacao ** 2
    
    return termo_esquerdo + termo_direito

if __name__ == "__main__":
    M_SOLAR = 1.989e30
    
    print("=" * 75)
    print("   LABORATÓRIO COMPUTACIONAL O ATEMPORAL - SIMULAÇÃO DA 20ª FORMA")
    print("=" * 75)
    
    # MODALIDADE 1: ESCALA REAL (M87* - 6.5 Bilhões de Massas Solares)
    massa_m87 = M_SOLAR * 6500000000
    print("MODO A: Telemetria Física Real (Objeto de Estudo: Monstro Supermassivo M87*)")
    print("Condição: Horizonte de Eventos Estático vs Kerr Real (z = 100.000)")
    print("-" * 75)
    
    r_estatico = calcular_telemetria_real_si(massa_m87, massa_m87, 100000.0, 0.0, 0)
    r_kerr = calcular_telemetria_real_si(massa_m87, massa_m87, 100000.0, 0.90, 17)
    
    # Conversão direta para Bilhões de Quilômetros (divisão por 1.000m e por 1.000.000.000 de km)
    bilhoes_km_estatico = r_estatico / 1e12
    bilhoes_km_kerr = r_kerr / 1e12
    
    print(f"-> M87* Schwarzschild Estático (theta=0°, chi=0.0): {bilhoes_km_estatico:.3f} Bilhões de km")
    print(f"-> M87* Kerr Dinâmico Real    (theta=17°, chi=0.90): {bilhoes_km_kerr:.3f} Bilhões de km")
    
    # MODALIDADE 2: MÉTRICA GEOMÉTRICA NORMALIZADA (R / r_s)
    print("\n" + "-" * 75)
    print("MODO B: Mapeamento de Camadas do Disco em Unidades Relativas (r_s)")
    print("Parâmetros da Maquete Quântica: Spin(chi) = 0.90 | Inclinação = 30°")
    print("-" * 75)
    
    camadas = [("Disco Externo", 0.10), ("Disco Intermediário", 0.41), 
               ("Limiar Dinâmico", 1.00), ("Borda Interna Extrema", 2.50)]
    
    for nome, z_obs in camadas:
        r_rs = calcular_raio_normalizado_rs(z_obs, 0.90, 30)
        print(f"-> {nome:<25} (z = {z_obs:.2f}) -> R ≈ {r_rs:.2f} r_s")
        
    print("=" * 75)
