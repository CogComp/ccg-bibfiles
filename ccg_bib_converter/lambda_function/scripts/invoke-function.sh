aws lambda invoke \
  --function-name ccg-bib-convert \
  --invocation-type RequestResponse \
  --payload '{"bib_str": "@article{test, title={{Sample size requirements for estimating Pearson, Kendall and Spearman correlations}}, author={Bonett, Douglas G and Wright, Thomas A}, journal={Psychometrika}, volume={65},number={1},pages={23--28},year={2000},publisher={Springer}}"}' \
  output.txt