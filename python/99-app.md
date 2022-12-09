# pdf2docx
```bash
pip install pdf2docx
```



```bash
# Convert all pages:
pdf2docx convert test.pdf test.docx
# Convert pages from the second to the end:
pdf2docx convert test.pdf test.docx --start=1
pdf2docx convert test.pdf test.docx --start=1 --end=3

# Convert the first, third and 5th pages:
pdf2docx convert test.pdf test.docx --pages=0,2,4
```

```bash
for i in *.pdf # $(ls)
do
	pdf2docx convert $i $i.docx
done
```

