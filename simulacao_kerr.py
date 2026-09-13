"""
===============================================================================
LABORATÓRIO COMPUTACIONAL COMPLETO - MÉTRICA DE KERR REAL (M87*)
Desenvolvido em Python Puro - Compatibilidade Total com Compiladores Online.
===============================================================================
"""

import math

def calcular_raio_kerr_real_si(M_campo, chi, theta_graus):
    """
    Calcula o raio físico do horizonte de eventos de Kerr em metros (SI).
    Aplica a física real de Einstein onde o horizonte encolhe com o spin.
    """
    G = 6.67430e-11  # Constante Gravitacional de Newton
    c = 299792458    # Velocidade da Luz
    
    # Converte a massa física para unidades geometrizadas (M em metros) -> G*M/c^2
    M_geom = (G * M_campo) / (c**2)
    
    # Trava de segurança para impedir erros de arredondamento em chi = 1.0
    if chi > 1.0:
        chi = 1.0
        
    # Parâmetro de rotação real (a)
    a = chi * M_geom
    
    # CORREÇÃO DA MÉTRICA DE KERR REAL: O spin subtrai dentro da raiz
    # Se chi = 0.0, a raiz dá M. Se chi = 1.0, a raiz dá 0.
    termo_raiz = math.sqrt(max(0.0, M_geom**2 - a**2))
    
    # Raio Geométrico Base (R+)
    r_base_metros = M_geom + termo_raiz
    
    # Correção do Ângulo de Observação (Efeito de Lente Gravitacional/Ergosfera)
    theta = math.radians(theta_graus)
    termo_angular = M_geom * (math.sin(theta)**2)
    
    # Retorna o raio final em metros somando a distorção visual da inclinação
    return r_base_metros + termo_angular

def calcular_camada_disco_normalizada(z, chi, theta_graus):
    """
    Calcula o raio de uma camada do disco de acreção em múltiplos de r_s.
    Mostra a maquete quântica de dentro para fora.
    """
    theta = math.radians(theta_graus)
    
    # Em escala normalizada de Schwarzschild, o raio base M = 1.0 (Rs = 2.0)
    M = 1.0
    a = chi * M
    
    # Horizonte geométrico encolhido na maquete
    r_plus = M + math.sqrt(max(0.0, M**2 - a**2))
    
    # Correção física do Redshift: quanto menor o z, mais distante a camada está
    fator_redshift = 1.0 + (1.0 / (z + 0.05))
    termo_angular = 0.5 * (math.sin(theta)**2)
    
    return (r_plus * fator_redshift) + termo_angular

if __name__ == "__main__":
    # Massa de referência: 1 Sol em Quilogramas
    M_SOLAR = 1.989e30
    
    # Massa do Monstro Supermassivo M87* (6.5 Bilhões de Sóis)
    massa_m87 = M_SOLAR * 6500000000
    
    print("=" * 75)
    print("   LABORATÓRIO COMPUTACIONAL CORRIGIDO - MÉTRICA DE KERR REAL")
    print("=" * 75)
    
    # -------------------------------------------------------------------------
    # MODO A: ESCALA FÍSICA REAL (VALIDAÇÃO COM A TABELA CIENTÍFICA)
    # -------------------------------------------------------------------------
    print("MODO A: Telemetria Física Real (Objeto de Estudo: Supermassivo M87*)")
    print("-" * 75)
    
    # Cenário 1: Totalmente Parado (Schwarzschild Puro - theta=0, chi=0.0)
    r_estatico_m = calcular_raio_kerr_real_si(massa_m87, 0.0, 0)
    
    # Cenário 2: Rotação de 90% visto de cima (Geometria Pura - theta=0, chi=0.90)
    r_kerr_90_polo_m = calcular_raio_kerr_real_si(massa_m87, 0.90, 0)
    
    # Cenário 3: Rotação de 90% Visto da Terra (Com Ângulo Real - theta=17, chi=0.90)
    r_kerr_90_terra_m = calcular_raio_kerr_real_si(massa_m87, 0.90, 17)
    
    # Cenário 4: Rotação Máxima Absoluta (Kerr Limite - theta=0, chi=1.0)
    r_kerr_max_m = calcular_raio_kerr_real_si(massa_m87, 1.0, 0)
    
    # Conversão das métricas de metros para Bilhões de Quilômetros (divisão por 1e12)
    b_km_estatico = r_estatico_m / 1e12
    b_km_kerr_90_polo = r_kerr_90_polo_m / 1e12
    b_km_kerr_90_terra = r_kerr_90_terra_m / 1e12
    b_km_kerr_max = r_kerr_max_m / 1e12
    
    print(f"-> M87* Estático (Sem Rotação)       : {b_km_estatico:.3f} Bilhões de km  | Tabela: ~19.2")
    print(f"-> M87* Rotação 90% (Geometria Pura)  : {b_km_kerr_90_polo:.3f} Bilhões de km  | Tabela: ~13.8")
    print(f"-> M87* Rotação 90% (Visto da Terra)  : {b_km_kerr_90_terra:.3f} Bilhões de km  | Lente Visível")
    print(f"-> M87* Rotação Máxima (Spin = 1.0)   : {b_km_kerr_max:.3f} Bilhões de km  | Tabela: ~9.6")
    
    # -------------------------------------------------------------------------
    # NOVO: GRÁFICO VISUAL EM MODO TEXTO (MATPLOTLIB EM CARACTERES)
    # -------------------------------------------------------------------------
    print("\n" + "-" * 75)
    print("GRÁFICO DA CONTRAÇÃO DO HORIZONTE DE EVENTOS PELO SPIN (M87*):")
    print("-" * 75)
    
    # Define barras proporcionais aos tamanhos calculados para desenhar na tela
    barra_estatica = "█" * int(b_km_estatico * 1.5)
    barra_kerr_90   = "█" * int(b_km_kerr_90_polo * 1.5)
    barra_kerr_max  = "█" * int(b_km_kerr_max * 1.5)
    
    print(f"Estático (chi=0.0) | {barra_estatica} {b_km_estatico:.1f} Bi km [Máximo Teórico]")
    print(f"Rotação  (chi=0.9) | {barra_kerr_90} {b_km_kerr_90_polo:.1f} Bi km [Redução de ~28%]")
    print(f"Máximo   (chi=1.0) | {barra_kerr_max} {b_km_kerr_max:.1f} Bi km [Metade do Tamanho!]")
    
    # -------------------------------------------------------------------------
    # MODO B: MAPEAMENTO DE CAMADAS DO DISCO (MAQUETE ADIMENSIONAL)
    # -------------------------------------------------------------------------
    print("\n" + "-" * 75)
    print("MODO B: Mapeamento de Camadas do Disco em Unidades Relativas (r_s)")
    print("Parâmetros da Maquete: Spin(chi) = 0.90 | Inclinação Angular = 30°")
    print("-" * 75)
    
    camadas = [
        ("Disco Externo Afastado ", 0.10), 
        ("Disco Intermediário     ", 0.41), 
        ("Limiar Dinâmico Doppler", 1.00), 
        ("Borda Interna (ISCO)    ", 2.50)
    ]
    
    for nome, z_obs in camadas:
        r_rs = calcular_camada_disco_normalizada(z_obs, 0.90, 30)
        print(f"-> {nome} (z = {z_obs:.2f}) -> R ≈ {r_rs:.2f} r_s")
        
    print("=" * 75)
