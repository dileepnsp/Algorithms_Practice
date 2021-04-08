import ply.lex as lex, re

tokens = (
    "TABLE",
    "JOIN",
    "COLUMN",
    "TRASH"
)

tables = {"tables": {}, "alias": {}}
columns = []

t_TRASH = r"Select|on|=|;|\s+|,|\t|\r"

def t_TABLE(t):
    r"from\s(\w+)\sas\s(\w+)"

    regex = re.compile(t_TABLE.__doc__)
    m = regex.search(t.value)
    if m is not None:
        tbl = m.group(1)
        alias = m.group(2)
        tables["tables"][tbl] = ""
        tables["alias"][alias] = tbl

    return t

def t_JOIN(t):
    r"inner\s+join\s+(\w+)\s+as\s+(\w+)"

    regex = re.compile(t_JOIN.__doc__)
    m = regex.search(t.value)
    if m is not None:
        tbl = m.group(1)
        alias = m.group(2)
        tables["tables"][tbl] = ""
        tables["alias"][alias] = tbl
    return t

def t_COLUMN(t):
    r"(\w+\.\w+)"

    regex = re.compile(t_COLUMN.__doc__)
    m = regex.search(t.value)
    if m is not None:
        t.value = m.group(1)
        columns.append(t.value)
    return t

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))
    t.lexer.skip(len(t.value))

# here is where the magic starts
def mylex(inp):
    lexer = lex.lex()
    lexer.input(inp)

    for token in lexer:
        pass

    result = {}
    for col in columns:
        tbl, c = col.split('.')
        if tbl in tables["alias"].keys():
            key = tables["alias"][tbl]
        else:
            key = tbl

        if key in result:
            result[key].append(c)
        else:
            result[key] = list()
            result[key].append(c)

    print(result)
    # {'tb1': ['col1', 'col7'], 'tb2': ['col2', 'col8']}

#string = "Select a.col1, b.col2 from tb1 as a inner join tb2 as b on tb1.col7 = tb2.col8;"
query="Select TO_CHAR(a.tc_arrived_time,'yyyy'),'1970',NULL,(TRUNC(a.tc_arrived_time,'MI')-TRUNC(a.tc_called_time,'MI'))*1440)) tc_response_time,round(DECODE(TO_CHAR(a.tc_cleared_time,'yyyy'),'1970',NULL,(TRUNC(a.tc_cleared_time,'MI')-TRUNC(a.tc_arrived_time,'MI'))*1440)) tc_clearance_time,round(DECODE(TO_CHAR(a.tc_cleared_time,'yyyy'),'1970',NULL,(TRUNC(a.tc_cleared_time,'MI')-TRUNC(a.tc_called_time,'MI'))*1440)) tc_recovery_time,DECODE(TO_CHAR(a.tc_arrived_time,'yyyy'),'1970',NULL,TO_CHAR(a.tc_arrived_time,'HH24:MI')) str_tc_arrived_time,DECODE(TO_CHAR(a.tc_cleared_time,'YYYY'),'1970',NULL,TO_CHAR(a.tc_cleared_time,'HH24:MI')) str_tc_cleared_time,DECODE(TO_CHAR(a.otc_arrived_time,'yyyy'),'1970',NULL,TO_CHAR(a.otc_arrived_time,'HH24:MI')) str_otc_arrived_time,DECODE(TO_CHAR(a.otc_cleared_time,'yyyy'),'1970',NULL,TO_CHAR(a.otc_cleared_time,'HH24:MI')) str_otc_cleared_time,round(DECODE(TO_CHAR(a.otc_arrived_time,'yyyy'),'1970',NULL,(TRUNC(a.otc_arrived_time,'MI')-TRUNC(a.tc_called_time,'MI'))*1440)) otc_response_time,round(DECODE(TO_CHAR(a.otc_cleared_time,'yyyy'),'1970',NULL,(TRUNC(a.otc_cleared_time,'MI')-TRUNC(a.otc_arrived_time,'MI'))*1440)) otc_clearance_time,	  round(DECODE(TO_CHAR(a.otc_cleared_time,'yyyy'),'1970',NULL,(TRUNC(a.otc_cleared_time,'MI')-TRUNC(a.tc_called_time,'MI'))*1440)) otc_recovery_time,To_char(tc_called_time,'hh24:mi')TC_CalledTime, START_DATE ,els_id ,CH ,DESCRIPTION ,ROAD_NAME,remarks ,SUBTYPE_DESCRIPTION ,TYPEDESCRIPTION ,Towed_Vehicle_Category ,Towing_Type_Id,Towing_Vehicle_Number,Towing_Company,Towed_Vehicle_Number,IR_TOWING_TYPE_CODE ,towing_type_desc,(case when VEHICLE_CATEGORY_ID=7 then null else a.VEHICLE_CATEGORY_ID end) as veh_cat,ir_id,direction, direction_displayfrom(SELECT CASE WHEN TOWING_TYPE.IR_TOWING_TYPE_CODE=2 OR TOWING_TYPE.TOWING_TYPE_ID=42 THEN HIST_TOW.Arrival_Time ELSE NULL END OTC_ARRIVED_TIME,CASE WHEN TOWING_TYPE.IR_TOWING_TYPE_CODE=2 OR TOWING_TYPE.TOWING_TYPE_ID=42 THEN HIST_TOW.Departure_Time ELSE NULL END OTC_CLEARED_TIME,Case when IR_TOWING_TYPE_CODE !=2 OR TOWING_TYPE.TOWING_TYPE_ID !=42 THEN HIST_TOW.Arrival_Time ELSE NULL END TC_ARRIVED_TIME,Case when TOWING_TYPE.IR_TOWING_TYPE_CODE !=2 OR TOWING_TYPE.TOWING_TYPE_ID !=42 THEN HIST_TOW.Departure_Time ELSE NULL END TC_CLEARED_TIME,to_char(a.start_time,'DD-MM-YYYY') START_DATE,a.ir_id,(a.els_id1||','||a.els_id2) els_id,a.down_point CH,E.DESCRIPTION,D.DESCRIPTION ROAD_NAME,F.comment_TEXT remarks,IR_SUBTYPE.DESCRIPTION SUBTYPE_DESCRIPTION,IR_TYPE.DESCRIPTION TYPEDESCRIPTION,b.direction, b.direction_display,HIST_TOW.Notification_Time tc_called_time,TOW_cAT.Description Towed_Vehicle_Category,TOW_CAT.VEHICLE_CATEGORY_ID,HIST_TOW.Towing_Vehicle_Number,HIST_TOW.Towing_Company,HIST_TOW.Towed_Vehicle_Number,TOWING_TYPE.IR_TOWING_TYPE_CODE ,TOWING_TYPE.TOWING_TYPE_ID ,Towing_type.description towing_type_desc from HIST_IR a, HIST_IR_ACCIDENT_DETAILS ACC_details, location_configuration b, location_code c, road_configuration_code d, IR_SOURCE E, HIST_IR_COMMENT F , IR_TYPE_SUBTYPE_MAPPING IR_SUBTYPE_MAPPING, IR_TYPE IR_TYPE, IR_SUBTYPE IR_SUBTYPE, HIST_IR_TOWING_VEHICLE HIST_TOW,IR_TOWING_VEHICLE_CATEGORY TOW_CAT,IR_TOWING_TYPE TOWING_TYPE  where ACC_details.ir_id = a.ir_id  and a.location_id = b.location_id and b.location_code_id = c.location_code_id and b.road_configuration_code_id = d.road_configuration_code_id  AND a.ir_source_id= E.IR_SOURCE_ID  AND A.IR_TYPE_SUBTYPE_MAPPING_ID = IR_SUBTYPE_MAPPING.IR_TYPE_SUBTYPE_ID  AND A.IR_ID = F.IR_ID(+)  AND IR_SUBTYPE_MAPPING.IR_TYPE_ID = IR_TYPE.IR_TYPE_ID   AND IR_SUBTYPE_MAPPING.IR_SUBTYPE_ID = IR_SUBTYPE.IR_SUBTYPE_ID  AND A.IR_ID = HIST_TOW.IR_ID   AND HIST_TOW.TOWED_VEHICLE_CATEGORY_ID = TOW_CAT.VEHICLE_CATEGORY_ID  AND HIST_TOW.TOWING_TYPE_ID = TOWING_TYPE.TOWING_TYPE_ID  and ir_type_code='0' and location_type in('0','1','4')"
mylex(query)