Link do site de configuração do VIRTUAL ENV : https://cloud.google.com/python/setup?hl=pt-br

CONFIGURAR MAQUINA COM AS SEGUINTES BIBLIOTECAS EM UMA MAQUINA VIRTUAL(VIRTUAL ENV):
    -Python 3.X
    -Pip Install 3.x

    Package               Version  
    --------------------- ---------
    argcomplete           1.8.2    
    arrow                 0.14.2   
    beautifulsoup4        4.5.3    
    certifi               2019.6.16
    chardet               3.0.4    
    docx2txt              0.6      
    EbookLib              0.15     
    idna                  2.8      
    lxml                  4.3.4    
    natsort               6.0.0    
    numpy                 1.16.4   
    opencv-contrib-python 4.1.0.25 
    pdfminer.six          20181108 
    pdftotext             2.1.1    
    Pillow                6.0.0    
    pip                   19.1.1   
    pycryptodome          3.8.2    
    PyPDF2                1.26.0   
    pytesseract           0.2.7    
    python-dateutil       2.8.0    
    python-pptx           0.6.5    
    regex                 2019.6.8 
    requests              2.22.0   
    selenium              3.141.0  
    setuptools            41.0.1   
    six                   1.10.0   
    sortedcontainers      2.1.0    
    SpeechRecognition     3.6.3    
    times                 0.7      
    urllib3               1.25.3   
    wheel                 0.33.4   
    xlrd                  1.0.0    
    XlsxWriter            1.1.8    

O que fazer:
    -Fazer com o que o PDFTOTEXT leia todos os PDF's (Algoritimo para ler o primeiro; Mudar nomeclatura, Mudar endereço).
    -Função para salvar todas as strings em um arquivo definitivo.
    -Função para excluir PDF's temporarios, após salva-lo os dados definitivos. 
    -Tratar de possíveis erros(HTTPS//HostConection//Captcha//Failed).
    -Colocar formatação da string do PDF em somente uma variavel.
    -Limitar loop do scrap, em um limite de 99. Quando o loop for <= 99, fazer com que quebre o loop e pule para a função que sera capaz de fazer scrap do PDF; Extraido os dados do PDF, mandar ao banco ele ira excluir os 99 PDF's baixados e executar a função Web Scrap novamente, retornando para o (loop anterior)loop do scrap.