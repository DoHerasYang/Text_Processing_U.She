#!/bin/sh
echo "Binary Result" >> show.txt
python ir_engine.py -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt
echo "Binary -p Result" >> show.txt
python ir_engine.py -p -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt
echo "Binary -s Result" >> show.txt
python ir_engine.py -s -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt
echo "Binary -s -p Result" >> show.txt
python ir_engine.py -p -s -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt

echo "TF Result" >> show.txt
python ir_engine.py -w tf -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt
echo "TF -p Result" >> show.txt
python ir_engine.py -w tf -p -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt
echo "TF -s Result" >> show.txt
python ir_engine.py -w tf -s -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt
echo "TF -s -p Result" >> show.txt
python ir_engine.py -w tf -p -s -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt

echo "TFIDF Result" >> show.txt
python ir_engine.py -w tfidf -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt
echo "TFIDF -p Result" >> show.txt
python ir_engine.py -w tfidf -p -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt
echo "TFIDF -s Result" >> show.txt
python ir_engine.py -w tfidf -s -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt
echo "TFIDF -s -p Result" >> show.txt
python ir_engine.py -w tfidf -p -s -o result.txt >> show.txt
python eval_ir.py cacm_gold_std.txt result.txt >> show.txt


