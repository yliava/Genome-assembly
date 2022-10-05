# hse22_hw1
  Создание ссылок  
  
      ln -s /usr/share/data-minor-bioinf/assembly/oil_R1.fastq
      ln -s /usr/share/data-minor-bioinf/assembly/oil_R2.fastq  
      ln -s /usr/share/data-minor-bioinf/assembly/oilMP_S4_L001_R1_001.fastq  
      ln -s /usr/share/data-minor-bioinf/assembly/oilMP_S4_L001_R2_001.fastq
 С помощью команды seqtk выбраны случайно 5 миллионов чтений типа paired-end
 
    seqtk sample -s126 oil_R1.fastq 5000000 > paired_end_R1.fastq
    seqtk sample -s126 oil_R2.fastq 5000000 > paired_end_R2.fastq
С помощью команды seqtk выбраны 1.5 миллиона чтений типа mate-pairs

    seqtk sample -s126 oilMP_S4_L001_R1_001.fastq 1500000 > mate_pairs_R1.fastq
    seqtk sample -s126 oilMP_S4_L001_R2_001.fastq 1500000 > mate_pairs_R2.fastq
Применение программы FastQC для оценки качества исходных чтений

    mkdir fastqc
    ls paired_end_R* mate_pairs_R* | xargs -P 4 -tI{} fastqc -o fastqc {}
Создание отчета через MultiQC

    mkdir multiqc
    multiqc -o multiqc fastqc
С помощью программ platanus_trim и platanus_internal_trim подрезаны чтения по качеству и удалены адаптеры

    platanus_trim paired_end_R*
    platanus_internal_trim mate_pairs_R*
Оценка качества обрезанных чтений с помощью FastQC

    mkdir fastqc_trimmed
    ls paired_end_R* mate_pairs_R*| xargs -P 4 -tI{} fastqc -o fastqc_trimmed {}
Создание отчета для обрезанных чтений через MultiQC

    mkdir multiqc_trimmed
    multiqc -o multiqc_trimmed fastqc_trimmed
Сбор контиг с помощью программы “platanus assemble”

    time platanus assemble -o Poil -f paired_end_R1.fastq.trimmed paired_end_R2.fastq.trimmed 2> assemble.log
Сбор скаффолдов с помощью “platanus scaffold”

    time platanus scaffold -o Poil -c Poil_contig.fa -IP1 paired_end_R1.fastq.trimmed paired_end_R2.fastq.trimmed -OP2 mate_pairs_R1.fastq.int_trimmed mate_pairs_R2.fastq.int_trimmed 2> scaffold.log
Уменьшение кол-ва гэпов с помощью подрезанных чтений, используя программу “platanus gap_close”

    time platanus gap_close -o Poil -c Poil_scaffold.fa -IP1 paired_end_R1.fastq.trimmed paired_end_R2.fastq.trimmed -OP2 mate_pairs_R1.fastq.int_trimmed mate_pairs_R2.fastq.int_trimmed 2> gapclose.log
**Статистика, полученная с помощью MultiQC, для исходных чтений**  
![2022-10-05_19-53-14](https://user-images.githubusercontent.com/90405153/194134759-5c307807-3d69-4d28-8c97-e92c84d8704e.png)
![fastqc_per_sequence_quality_scores_plot](https://user-images.githubusercontent.com/90405153/194135187-074583d7-8e2e-4537-9bd4-deeea630d87a.png)
![fastqc_adapter_content_plot](https://user-images.githubusercontent.com/90405153/194135205-f9a71dd6-cc17-411d-9fdb-49e5f2a736b7.png)

**Статистика, полученная с помощью MultiQC, для подрезанных чтений**
![2022-10-05_20-55-22](https://user-images.githubusercontent.com/90405153/194135388-728346e1-c065-4838-8a0e-a41e88ce94f2.png)
![fastqc_per_sequence_quality_scores_plot (1)](https://user-images.githubusercontent.com/90405153/194135415-60ca4fec-f5e6-4bd3-9541-a6e5aa3460fd.png)
![fastqc_adapter_content_plot (1)](https://user-images.githubusercontent.com/90405153/194135439-56c5d7e5-ed20-422e-8799-d26a22a26c98.png)

# Google Colab
https://colab.research.google.com/drive/1iYPaxl4C9woSE8TpFSUiYQYUT5oYekVX?usp=sharing

