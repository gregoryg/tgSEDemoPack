for i in allergies careplans conditions demographics devices encounters imaging_studies immunizations medications normalizedSymptoms observations organizations patients payer_transitions payers procedures providers zipcodes
do
    cat "$i"*copy.csv.header > "$i".csv
    cat "$i"*copy.csv >> "$i".csv
done

rm -rf *copy*