"""
===============================================================================
SISTEMA DE TELEMETRIA RADIAL NORMALIZADA - MÓDULO IV (MÉTRICA DE KERR RELATIVA)
Princípio da Proporcionalidade Inversa (Antônio Marcos, 2026 - CC BY 4.0)

Mapeamento de Distância em Unidades Relativas do Raio de Schwarzschild (r_s).
Modelagem, Unificação de Campo (m ≡ M) e Revisão por: [Seu Nome / Nickname]
===============================================================================
"""

import math

def calcular_raio_normalizado(z, chi, theta_graus):
    """
    Calcula a distância telemétrica normalizada diretamente em múltiplos de r_s.
    Elimina a necessidade de injetar constantes físicas como G, c e a massa.
    """
    # Conversão do ângulo orbital para radianos
    theta = math.radians(theta_graus)
    
    # 1. Base Relativa: Em múltiplos de r_s, o termo (raiz_base) é exatamente 1.0
    base_relativa = 1.0
    
    # 2. Fator de Correção de Spin (Efeito de Rotação de Kerr)
    fator_spin = 2 / (1 + math.sqrt(1 - chi**2))
    
    # 3. Filtro do Redshift Gravitacional (Ajuste Telemétrico Inverso no Denominador)
    fator_redshift = 1 - (1 / (z + 1)**2)
    
    # 4. Projeção de Inclinação Orbital (Efeito Analítico de Lente Gravitacional)
    # Em termos normalizados de r_s, o fator da gravidade reduz-se a 0.5 * sin(theta)
    fator_inclinacao = 0.5 * math.sin(theta)
    
    # Polinômio Estrutural Adaptado da 20ª Forma Relativa
    termo_esquerdo = (base_relativa * fator_spin) / fator_redshift
    termo_direito = fator_inclinacao ** 2
    
    R_normalizado = termo_esquerdo + termo_direito
    return R_normalizado


if __name__ == "__main__":
    print("=" * 70)
    print("     SIMULAÇÃO COMPUTACIONAL EM MÉTRICA DE RAIO (R / r_s)")
    print("======================================================================")
    print("Configuração Base da Imagem: Spin(chi) = 0.90 | Inclinação(theta) = 30°")
    print("-" * 70)
    
    # Camadas exatas de amostragem da tabela que você renderizou na I.A.
    camadas_analise = [
        {"nome": "Disco Externo", "z": 0.10},
        {"nome": "Disco Intermediário", "z": 0.41},
        {"nome": "Limiar Dinâmico", "z": 1.00},
        {"nome": "Borda Interna Extrema", "z": 2.50}
    ]
    
    for camada in camadas_analise:
        r_rs = calcular_raio_normalizado(
            z=camada["z"], 
            chi=0.90, 
            theta_graus=30
        )
        print(f"{camada['nome']:<25} (z = {camada['z']:.2f}) -> R ≈ {r_rs:.2f} r_s")
    
    print("=" * 70)
