FROM python:3.12

RUN pip3 install biopython pydantic

COPY fasta_stats.py /code/fasta_stats.py
COPY fasta_filter.py /code/fasta_filter.py
COPY fastq_filter.py /code/fastq_filter.py
COPY mmcif_summary.py /code/mmcif_summary.py

RUN chmod ugo+x /code/fasta_stats.py /code/fasta_filter.py /code/fastq_filter.py /code/mmcif_summary.py

ENV PATH="/code:$PATH"