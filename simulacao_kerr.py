"""
===============================================================================
LABORATÓRIO COMPUTACIONAL O ATEMPORAL - VERSÃO DEFINITIVA COMPLETA
Princípio da Proporcionalidade Inversa (Antônio Marcos, 2026 - CC BY 4.0)

Gráfico com Rotação Máxima (chi=1.0) e Modo B 100% Corrigido.
===============================================================================
"""

import math

def calcular_raio_oficial_definitivo(M_campo, m_fluxo, z, chi, theta_graus):
    """
    Calcula o raio da imagem da sombra telemétrica baseada na fórmula do livro.
    """
    G = 6.67430e-11
    c = 299792458
    theta = math.radians(theta_graus)
    
    k = (c**7) / (4 * (G**2) * M_campo)
    termo_fluxo = math.sqrt((m_fluxo * (c**3)) / k)
    
    if chi > 1.0: 
        chi = 1.0
    
    fator_spin = 2 / (1 + math.sqrt(max(0.0, 1 - chi**2)))
    fator_redshift = 1 - (1 / (z + 1)**2)
    if fator_redshift == 0: 
        fator_redshift = 1e-10
        
    denominador_total = fator_redshift * fator_spin
    raiz_grande_esquerda = math.sqrt(max(0.0, termo_fluxo / denominador_total))
    
    bloco_seno_direito = math.sqrt((G * M_campo) / (c**2)) * math.sin(theta)
    
    # Produto Notável original (+): Expansão óptica da lente
    R_final = (raiz_grande_esquerda + bloco_seno_direito) ** 2
    
    return R_final

def calcular_camada_disco_normalizada(z, chi, theta_graus):
    """
    Calcula o raio de uma camada do disco de acreção em múltiplos de r_s.
    CORRIGIDO: Sem erros de digitação nas variáveis.
    """
    theta = math.radians(theta_graus)
    M = 1.0
    a = chi * M
    r_plus = M + math.sqrt(max(0.0, M**2 - a**2))
    
    # Nome correto da variável com 'c'
    fator_redshift = 1.0 + (1.0 / (z + 0.05))
    termo_angular = 0.5 * (math.sin(theta)**2)
    
    return (r_plus * fator_redshift) + termo_angular

if __name__ == "__main__":
    M_SOLAR = 1.989e30
    massa_m87 = M_SOLAR * 6500000000  # 6.5 Bilhões de Massas Solares (M87*)
    z_limite = 100000.0                # Limite assintótico para isolar a geometria
    
    print("=" * 75)
    print("   LABORATÓRIO COMPUTACIONAL O ATEMPORAL - FORMULAÇÃO OFICIAL REVISADA")
    print("=" * 75)
    
    # Execução de todos os cenários, incluindo a rotação máxima
    r_estatico = calcular_raio_oficial_definitivo(massa_m87, massa_m87, z_limite, 0.0, 0)
    r_kerr_polo = calcular_raio_oficial_definitivo(massa_m87, massa_m87, z_limite, 0.90, 0)
    r_kerr_terra = calcular_raio_oficial_definitivo(massa_m87, massa_m87, z_limite, 0.90, 17)
    r_kerr_max = calcular_raio_oficial_definitivo(massa_m87, massa_m87, z_limite, 1.0, 0)
    
    b_km_estatico = r_estatico / 1e12
    b_km_kerr_polo = r_kerr_polo / 1e12
    b_km_kerr_terra = r_kerr_terra / 1e12
    b_km_kerr_max = r_kerr_max / 1e12
    
    print("MODO A: Telemetria Física Real (Objeto de Estudo: Supermassivo M87*)")
    print("-" * 75)
    print(f"-> M87* Estático (Sem Rotação)       : {b_km_estatico:.3f} Bilhões de km  | Tabela: ~19.2")
    print(f"-> M87* Rotação 90% (Geometria Pura)  : {b_km_kerr_polo:.3f} Bilhões de km  | Tabela: ~13.8")
    print(f"-> M87* Rotação 90% (Visto da Terra)  : {b_km_kerr_terra:.3f} Bilhões de km  | Imagem EHT Real")
    print(f"-> M87* Rotação Máxima (Spin = 1.0)   : {b_km_kerr_max:.3f} Bilhões de km  | Tabela: ~9.6")
    print("=" * 75)
    
    # Gráfico de barras atualizado com a linha de Rotação Máxima 1.0
    print("\n   GRAFICO DE BARRAS NO TERMINAL (MÉTRICA DA SOMBRA VISÍVEL):")
    print("-" * 75)
    print(f"Estático (chi=0.0) | " + "█" * int(b_km_estatico * 1.5) + f" {b_km_estatico:.1f} Bi km [Módulo Base]")
    print("Puro     (chi=0.9) | " + "█" * int(b_km_kerr_polo * 1.5) + f" {b_km_kerr_polo:.1f} Bi km [Contração Geométrica]")
    print("Máximo   (chi=1.0) | " + "█" * int(b_km_kerr_max * 1.5) + f"  {b_km_kerr_max:.1f} Bi km [Metade do Tamanho!]")
    print("Terra    (chi=0.9) | " + "█" * int(b_km_kerr_terra * 1.5) + f" {b_km_kerr_terra:.1f} Bi km [Expansão da Lente Óptica]")
    print("-" * 75)
    
    print("\nMODO B: Mapeamento de Camadas do Disco em Unidades Relativas (r_s)")
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
