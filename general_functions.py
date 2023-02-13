def uploading_files():
    """type: tuple. Realiza o upload de varios arquivos simultaneamente."""
    from google.colab import files
    uploaded = files.upload()
    uploaded_files = list(uploaded.keys())
    output_filename = [] 
    for file_name in uploaded_files:
        output_filename.append(file_name.replace('.xlsx', ".mf4"))
    return (uploaded_files, output_filename)

def uploading_single_file():
    """type: list. Realiza o upload de um único arquivo por vez."""
    from google.colab import files
    uploaded = files.upload()
    uploaded_file = list(uploaded.keys())[0]
    return uploaded_file

def subir_aquivo():
    """type: boolean. Validação de loop para subir arquivos"""
    repetir = ''
    while repetir.lower() != 's' and repetir.lower() != 'n':
        repetir = input('Deseja adicionar mais algum arquivo? s ou  n \n')
        if repetir.lower() != 's' and repetir.lower() != 'n':
            print('caractere inválido')

    if repetir.lower() == 's':
        return True
    elif repetir.lower() == 'n':
        return False
