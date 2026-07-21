# Excel Converter

Este diretório contém um projeto pessoal legado para converter planilhas Excel em arquivos PDF por meio de uma interface gráfica.

O projeto foi preservado em sua estrutura original. O código, a configuração de empacotamento e os artefatos existentes não foram modificados durante a preparação para versionamento.

## Organização

- `Excel converter.py`: código-fonte principal da aplicação.
- `Excel converter.spec`: configuração existente do PyInstaller.
- `icon.ico`: ícone utilizado pelo empacotamento.
- `build/`: arquivos intermediários gerados pelo PyInstaller; mantidos localmente e ignorados pelo Git.
- `dist/`: executável gerado; mantido localmente e ignorado pelo Git.

Consulte `PROJECTS.md` para o inventário técnico e as limitações conhecidas.

## Tecnologias detectadas

- Python 3.11 no build existente;
- Tkinter para a interface gráfica;
- pandas para leitura das planilhas;
- módulo `fpdf` para geração dos arquivos PDF;
- PyInstaller para geração do executável Windows.

O build também contém referências a `openpyxl` e `xlrd`, normalmente utilizados pelo pandas para formatos Excel. Não há manifesto de dependências nem versões confiáveis registradas para todos os pacotes, portanto nenhum comando de instalação é indicado aqui.

## Execução e validação

Não havia instruções de execução ou testes automatizados no conteúdo original. A aplicação e o executável existente não foram executados durante esta organização, e seu funcionamento atual não foi validado.

Antes de executar ou reconstruir o projeto, confirme as dependências em um ambiente virtual isolado. O arquivo `Excel converter.py` também possui uma referência absoluta a um ícone no ambiente original, o que pode exigir atenção em outro computador.

## Versionamento

Os diretórios `build/` e `dist/` são artefatos gerados e permanecem fora do versionamento. O arquivo `Excel converter.spec` e o ícone são preservados como entradas necessárias para uma futura reconstrução.

Nenhuma licença foi escolhida para este projeto.
