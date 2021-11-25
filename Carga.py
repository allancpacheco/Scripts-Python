
file = open('file.txt', 'w')

c = 0

while c < len(df):
   file.write('\ninsert into CBHPM_PRECO (NR_SEQUENCIA,DT_ATUALIZACAO,NM_USUARIO,CD_PROCEDIMENTO,IE_ORIGEM_PROCED,DT_VIGENCIA,CD_PORTE,TX_PORTE,QT_UCO,NR_PORTE_ANEST,NR_AUXILIAR,QT_FILME,QT_INCIDENCIA,IE_UNID_RA,DT_ATUALIZACAO_NREC,NM_USUARIO_NREC,CD_ESTABELECIMENTO) values ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(
         c,'sysdate',"'acpacheco'", df['CD_PROCEDIMENTO'][c], '5' , 'sysdate', "'" + str(df['CD_PORTE'][c]) + "'",'null', df['VL_CUSTO_OPERACIONAL'][c], df['NR_PORTE_ANEST'][c], df['NR_AUXILIAR'][c], df['QT_FILME'][c], df['QT_INCIDENCIA'][c], df['IE_UNID_RA'][c],
         'sysdate',"'acpacheco'",'1);'))
   c = c + 1

file.close()