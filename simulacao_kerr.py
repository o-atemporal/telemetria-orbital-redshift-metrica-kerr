"""
🌌 Telemetria para Inclinação Orbital e Redshift – Métricas de Kerr em Buracos Negros
Implementação oficial computacional do ecossistema O Atemporal.

Baseado nas soluções analíticas introduzidas na obra 'Equações de Fluxo Inverso'.
Autor Oficial: Antônio Marcos
Ano: 2026
Licença: Creative Commons Attribution 4.0 International (CC BY 4.0)
Repositorio: https://github.com
"""

__author__ = "Antônio Marcos (O Atemporal)"
__copyright__ = "Copyright 2026, O Atemporal"
__credits__ = ["Antônio Marcos"]
__license__ = "CC BY 4.0"
__version__ = "1.0.0"
__maintainer__ = "Antônio Marcos"
__status__ = "Production"

"""
===============================================================================
LABORATÓRIO COMPUTACIONAL O ATEMPORAL - SIMULADOR MULTI-ALVO COMPLETO
Princípio da Proporcionalidade Inversa (Antônio Marcos, 2026 - CC BY 4.0)

Formulação Oficial com Menu, Gráfico Adaptativo e Mapeamento do Disco (Modo B).
===============================================================================
"""

import math

def calcular_raio_oficial_definitivo(M_campo, m_fluxo, z, chi, theta_graus):
    """Calcula o raio da imagem da sombra baseado na fórmula do livro."""
    G = 6.67430e-11
    c = 299792458
    theta = math.radians(theta_graus)
    
    k = (c**7) / (4 * (G**2) * M_campo)
    termo_fluxo = math.sqrt((m_fluxo * (c**3)) / k)
    
    if chi > 1.0: chi = 1.0
    fator_spin = 2 / (1 + math.sqrt(max(0.0, 1 - chi**2)))
    fator_redshift = 1 - (1 / (z + 1)**2)
    if fator_redshift == 0: fator_redshift = 1e-10
        
    denominador_total = fator_redshift * fator_spin
    raiz_grande_esquerda = math.sqrt(max(0.0, termo_fluxo / denominador_total))
    bloco_seno_direito = math.sqrt((G * M_campo) / (c**2)) * math.sin(theta)
    
    return (raiz_grande_esquerda + bloco_seno_direito) ** 2

def calcular_camada_disco_normalizada(z, chi, theta_graus):
    """Calcula o raio de uma camada do disco em múltiplos de r_s de forma coerente."""
    theta = math.radians(theta_graus)
    M = 1.0
    a = chi * M
    r_plus = M + math.sqrt(max(0.0, M**2 - a**2))
    
    fator_redshift = 1.0 + (1.0 / (z + 0.05))
    termo_angular = 0.5 * (math.sin(theta)**2)
    
    return (r_plus * fator_redshift) + termo_angular

if __name__ == "__main__":
    M_SOLAR = 1.989e30
    
    # 🌌 BANCO DE DADOS DE OBJETOS REAIS (Massa Solar e Ângulo Científico Oficial)
    catalogo_objetos = {
        "1": {"nome": "M87* (Monstro Supermassivo)", "massa": 6500000000, "angulo_padrao": 15.0},
        "2": {"nome": "Sagittarius A* (Centro da Via Láctea)", "massa": 4300000, "angulo_padrao": 30.0},
        "3": {"nome": "Cygnus X-1 (Buraco Negro Estelar)", "massa": 21, "angulo_padrao": 27.0}
    }
    
    print("=" * 75)
    print("      SISTEMA INTERATIVO O ATEMPORAL - SELEÇÃO DE HORIZONTES DE KERR")
    print("=" * 75)
    print("Escolha o Buraco Negro para Simulação:")
    for chave, dados in catalogo_objetos.items():
        print(f" [{chave}] -> {dados['nome']}")
    print("=" * 75)
    
    opcao = input("Digite o número do objeto desejado (1, 2 ou 3): ").strip()
    if opcao not in catalogo_objetos:
        print("[AVISO]: Opção inválida. Adotando M87* por padrão.")
        opcao = "1"
        
    objeto = catalogo_objetos[opcao]
    massa_objeto = M_SOLAR * objeto["massa"]
    
    print(f"\nO ângulo de visão científico sugerido para o {objeto['nome']} é {objeto['angulo_padrao']}°.")
    customizar = input("Deseja alterar esse ângulo de visão? (s/n): ").strip().lower()
    
    if customizar == 's':
        try:
            angulo_usuario = float(input("Digite o novo ângulo de visão em graus: "))
        except ValueError:
            print("[AVISO]: Valor inválido. Mantendo ângulo sugerido.")
            angulo_usuario = objeto["angulo_padrao"]
    else:
        angulo_usuario = objeto["angulo_padrao"]
        
    # --- PROCESSAMENTO DOS CENÁRIOS (MODO A) ---
    z_limite = 100000.0
    r_estatico = calcular_raio_oficial_definitivo(massa_objeto, massa_objeto, z_limite, 0.0, 0)
    r_kerr_polo = calcular_raio_oficial_definitivo(massa_objeto, massa_objeto, z_limite, 0.90, 0)
    r_kerr_terra = calcular_raio_oficial_definitivo(massa_objeto, massa_objeto, z_limite, 0.90, angulo_usuario)
    r_kerr_max = calcular_raio_oficial_definitivo(massa_objeto, massa_objeto, z_limite, 1.0, 0)
    
    # --- DEFINIÇÃO DOS FATORES DE ESCALA E MULTIPLICADORES DO GRÁFICO ---
    if opcao == "1":
        fator_escala = 1e12  # Bilhões de km
        unidade = "Bi km"
        peso_barra = 1.5     # Proporção visual ideal para bilhões
    elif opcao == "2":
        fator_escala = 1e9   # Milhões de km
        unidade = "Milhões de km"
        peso_barra = 2.0     # Proporção visual ideal para milhões
    else:
        fator_escala = 1e3   # Quilômetros
        unidade = "km"
        peso_barra = 0.4     # Proporção visual ideal para metros/km
        
    b_km_estatico = r_estatico / fator_escala
    b_km_kerr_polo = r_kerr_polo / fator_escala
    b_km_kerr_terra = r_kerr_terra / fator_escala
    b_km_kerr_max = r_kerr_max / fator_escala
        
    print("\n" + "=" * 75)
    print(f"MODO A: Telemetria Física Real [{objeto['nome'].upper()}]")
    print("-" * 75)
    print(f"-> Horizonte Estático (chi=0.0) : {b_km_estatico:.3f} {unidade}")
    print(f"-> Contração de Kerr  (chi=0.9) : {b_km_kerr_polo:.3f} {unidade}")
    print(f"-> Sombra Visível     ({angulo_usuario}°) : {b_km_kerr_terra:.3f} {unidade} | Diâmetro: {b_km_kerr_terra*2:.3f} {unidade}")
    print(f"-> Rotação Máxima     (chi=1.0) : {b_km_kerr_max:.3f} {unidade}")
    print("=" * 75)
    
    # --- RENDERIZAÇÃO DO GRÁFICO DE BARRAS NO TERMINAL ---
    print("\n   GRAFICO DE BARRAS NO TERMINAL (MÉTRICA DA SOMBRA VISÍVEL):")
    print("-" * 75)
    print(f"Estático (chi=0.0) | " + "█" * int(b_km_estatico * peso_barra) + f" {b_km_estatico:.1f} {unidade}")
    print(f"Puro     (chi=0.9) | " + "█" * int(b_km_kerr_polo * peso_barra) + f" {b_km_kerr_polo:.1f} {unidade}")
    print(f"Máximo   (chi=1.0) | " + "█" * int(b_km_kerr_max * peso_barra) + f" {b_km_kerr_max:.1f} {unidade}")
    print(f"Terra    (chi=0.9) | " + "█" * int(b_km_kerr_terra * peso_barra) + f" {b_km_kerr_terra:.1f} {unidade} [Lente com {angulo_usuario}°]")
    print("-" * 75)
    
    # --- MODO B: MAPEAMENTO DE CAMADAS NORMALIZADAS EM R_S ---
    print("\nMODO B: Mapeamento de Camadas do Disco em Unidades Relativas (r_s)")
    print(f"Parâmetros da Maquete: Spin(chi) = 0.90 | Inclinação Orbital = {angulo_usuario}°")
    print("-" * 75)
    camadas = [
        ("Disco Externo Afastado ", 0.10), 
        ("Disco Intermediário     ", 0.41), 
        ("Limiar Dinâmico Doppler", 1.00), 
        ("Borda Interna (ISCO)    ", 2.50)
    ]
    for nome, z_obs in camadas:
        r_rs = calcular_camada_disco_normalizada(z_obs, 0.90, angulo_usuario)
        print(f"-> {nome} (z = {z_obs:.2f}) -> R ≈ {r_rs:.2f} r_s")
    print("=" * 75)
