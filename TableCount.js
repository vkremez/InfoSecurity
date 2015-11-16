table = new SimpleTable("___.csv");
table.convertToLowerCase();
count1 = 0;
count2 = 0;
for (row: table) {
   if (row.getField("___") == "___" &&
       row.getField("___") == "___"){
        count1 = count1 + 1;
  }
   if (row.getField("___") == "___" &&
       row.getField("___") == "___"){
        count2 = count2 + 1;
  }
}
print("count: ", count1);
print("count: ", count2);  
