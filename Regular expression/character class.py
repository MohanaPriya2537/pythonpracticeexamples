#[abc]->either a or b or c(ly a,b,c)

# import re
# matches=re.finditer('[abc]','a8b@9hz*')
# for m in matches:
#     print(m.start(),'....',m.group())


# [^abc]->except a and b and c
# import re
# matches=re.finditer('[^abc]','a8b@9hz*')
# for m in matches:
#     print(m.start(),'....',m.group())

# [a-z]->Any lowercase alphabet symbol
# import re
# matches=re.finditer('[a-z]','a8b@9hz*Y')
# for m in matches:
#     print(m.start(),'....',m.group())

# [A-Z]->Any uppercase alphabet symbol
# import re
# matches=re.finditer('[A-Z]','A8b@9hz*K')
# for m in matches:
#     print(m.start(),'....',m.group())

# [0-9]->Numeric
# import re
# matches=re.finditer('[0-9]','A8b@9hz*K')
# for m in matches:
#     print(m.start(),'....',m.group())

# [a-zA-Z]->Any alphabet symbol
# import re
# matches=re.finditer('[a-zA-Z]','A8b@9hz*K')
# for m in matches:
#     print(m.start(),'....',m.group())

# [a-zA-Z0-9]->Alphanumeric
# import re
# matches=re.finditer('[a-zA-Z0-9]','A8b@9hz*K')
# for m in matches:
#     print(m.start(),'....',m.group())

# [^a-zA-Z0-9]->Except alphanumeric

import re
matches=re.finditer('[^a-zA-Z0-9]','A8b@9hz*K')
for m in matches:
    print(m.start(),'....',m.group())