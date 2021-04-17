location_str = ["徐汇区虹漕路461号58号楼5楼", "泉州市洛江区万安塘西工业区", "北京朝阳区北苑华贸城"]
import json

import cpca

df = cpca.transform(["徐汇区虹漕路461号58号楼5楼"])
data = json.loads(df.to_json(orient="records",force_ascii=False))
print(data[0]['省'])
