from underthesea import ner

text1 = "Bệnh Alzheimer là nguyên nhân hàng đầu gây nên tình trạng sa sút trí tuệ, ảnh hưởng đến suy nghĩ và hành vi của con người. Không có cách nào để đảo ngược quá trình tiến triển bệnh, nhưng việc phát hiện và điều trị sớm có thể giúp nâng cao chất lượng cuộc sống cho người bệnh."

text2 = "Thống kê cho thấy trên thế giới có ít nhất 50 triệu người đang sống chung với bệnh Alzheimer hoặc các hội chứng sa sút trí tuệ khác. Theo Liên Hợp Quốc, con số đó nhiều hơn dân số của Columbia, nếu không có những đột phá trong việc chẩn đoán và hạn chế bệnh, tỷ lệ này có thể vượt quá 152 triệu người vào năm 2050."

print(ner(text1))
# [('Bệnh', 'N', 'B-NP', 'B-LOC'), ('Alzheimer', 'Np', 'B-NP', 'I-LOC'), ('là', 'V', 'B-VP', 'O'), ('nguyên nhân', 'N', 'B-NP', 'O'), ('hàng đầu', 'N', 'B-NP', 'O'), ('gây', 'V', 'B-VP', 'O'), ('nên', 'C', 'O', 'O'), ('tình trạng', 'N', 'B-NP', 'O'), ('sa sút', 'V', 'B-VP', 'O'), ('trí tuệ', 'N', 'B-NP', 'O'), (',', 'CH', 'O', 'O'), ('ảnh hưởng', 'V', 'B-VP', 'O'), ('đến', 'E', 'B-PP', 'O'), ('suy nghĩ', 'V', 'B-VP', 'O'), ('và', 'C', 'O', 'O'), ('hành vi', 'N', 'B-NP', 'O'), ('của', 'E', 'B-PP', 'O'), ('con người', 'N', 'B-NP', 'O'), ('.', 'CH', 'O', 'O'), ('Không', 'R', 'O', 'O'), ('có', 'V', 'B-VP', 'O'), ('cách', 'N', 'B-NP', 'O'), ('nào', 'P', 'B-NP', 'O'), ('để', 'E', 'B-PP', 'O'), ('đảo ngược', 'V', 'B-VP', 'O'), ('quá trình', 'N', 'B-NP', 'O'), ('tiến triển', 'V', 'B-VP', 'O'), ('bệnh', 'N', 'B-NP', 'O'), (',', 'CH', 'O', 'O'), ('nhưng', 'C', 'O', 'O'), ('việc', 'N', 'B-NP', 'O'), ('phát hiện', 'V', 'B-VP', 'O'), ('và', 'C', 'O', 'O'), ('điều trị', 'V', 'B-VP', 'O'), ('sớm', 'A', 'B-AP', 'O'), ('có thể', 'R', 'O', 'O'), ('giúp', 'V', 'B-VP', 'O'), ('nâng', 'V', 'B-VP', 'O'), ('cao', 'A', 'B-AP', 'O'), ('chất lượng', 'N', 'B-NP', 'O'), ('cuộc sống', 'N', 'B-NP', 'O'), ('cho', 'E', 'B-PP', 'O'), ('người bệnh', 'N', 'B-NP', 'O'), ('.', 'CH', 'O', 'O')]
print(ner(text2))
# [('Thống kê', 'N', 'B-NP', 'O'), ('cho', 'V', 'B-VP', 'O'), ('thấy', 'V', 'B-VP', 'O'), ('trên', 'E', 'B-PP', 'O'), ('thế giới', 'N', 'B-NP', 'O'), ('có', 'V', 'B-VP', 'O'), ('ít nhất', 'X', 'O', 'O'), ('50', 'M', 'B-NP', 'O'), ('triệu', 'M', 'B-NP', 'O'), ('người', 'N', 'B-NP', 'O'), ('đang', 'R', 'O', 'O'), ('sống', 'V', 'B-VP', 'O'), ('chung', 'A', 'B-AP', 'O'), ('với', 'E', 'B-PP', 'O'), ('bệnh', 'N', 'B-NP', 'O'), ('Alzheimer hoặc', 'V', 'B-VP', 'O'), ('các', 'L', 'B-NP', 'O'), ('hội chứng', 'N', 'B-NP', 'O'), ('sa sút', 'V', 'B-VP', 'O'), ('trí tuệ', 'N', 'B-NP', 'O'), ('khác', 'A', 'B-AP', 'O'), ('.', 'CH', 'O', 'O'), ('Theo', 'V', 'B-VP', 'B-PER'), ('Liên Hợp Quốc', 'Np', 'B-NP', 'I-PER'), (',', 'CH', 'O', 'O'), ('con số', 'N', 'B-NP', 'O'), ('đó', 'P', 'B-NP', 'O'), ('nhiều', 'A', 'B-AP', 'O'), ('hơn', 'A', 'B-AP', 'O'), ('dân số', 'N', 'B-NP', 'O'), ('của', 'E', 'B-PP', 'O'), ('Columbia', 'Np', 'B-NP', 'B-PER'), (',', 'CH', 'O', 'O'), ('nếu', 'C', 'O', 'O'), ('không', 'R', 'O', 'O'), ('có', 'V', 'B-VP', 'O'), ('những', 'L', 'B-NP', 'O'), ('đột phá', 'N', 'B-NP', 'O'), ('trong', 'E', 'B-PP', 'O'), ('việc', 'N', 'B-NP', 'O'), ('chẩn đoán', 'V', 'B-VP', 'O'), ('và', 'C', 'O', 'O'), ('hạn chế', 'V', 'B-VP', 'O'), ('bệnh', 'N', 'B-NP', 'O'), (',', 'CH', 'O', 'O'), ('tỷ lệ', 'N', 'B-NP', 'O'), ('này', 'P', 'B-NP', 'O'), ('có thể', 'R', 'O', 'O'), ('vượt', 'V', 'B-VP', 'O'), ('quá', 'R', 'O', 'O'), ('152', 'M', 'B-NP', 'O'), ('triệu', 'M', 'B-NP', 'O'), ('người', 'N', 'B-NP', 'O'), ('vào', 'E', 'B-PP', 'O'), ('năm', 'N', 'B-NP', 'B-LOC'), ('2050', 'M', 'B-NP', 'I-LOC'), ('.', 'CH', 'O', 'O')]