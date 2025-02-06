import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrameCollection
from awsglue.dynamicframe import DynamicFrame

# Script generated for node Custom Transform
def MyTransform(glueContext, dfc) -> DynamicFrameCollection:
       
    from pyspark.ml.feature import StringIndexer
    # Convert the incoming DynamicFrame to a Spark DataFrame
    demographics_dyf = dfc.select(list(dfc.keys())[0]).toDF()

    # Create a StringIndexer instance
    indexer = StringIndexer(
        inputCol="rucc_category",  # Input column
        outputCol="rucc_category_index",  # Output column
        handleInvalid="keep"  # Handle invalid values gracefully
    )

    # Apply StringIndexer transformation
    transformed_df = indexer.fit(demographics_dyf).transform(demographics_dyf)

    # Drop the original column and rename the indexed column
    transformed_df = (
        transformed_df.drop("rucc_category")
                      .withColumnRenamed("rucc_category_index", "rucc_category")
    )

    # Convert back to a DynamicFrame
    transformed_dyf = DynamicFrame.fromDF(transformed_df, glueContext, "transformed_demographics")

    # Return the transformed DynamicFrame as a collection
    return DynamicFrameCollection({"transformed_demographics": transformed_dyf}, glueContext)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Cost & Utilization
CostUtilization_node1738874585187 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://humanaproject/staging/Cost & Utilization.csv"], "recurse": True}, transformation_ctx="CostUtilization_node1738874585187")

# Script generated for node Demographics
Demographics_node1738874840681 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://humanaproject/staging/Demographics.csv"], "recurse": True}, transformation_ctx="Demographics_node1738874840681")

# Script generated for node target_members
target_members_node1738873669735 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://humanaproject/staging/humana_mays_target_members.csv"], "recurse": True}, transformation_ctx="target_members_node1738873669735")

# Script generated for node Additional Features
AdditionalFeatures_node1738827123247 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://humanaproject/staging/Additional Features.csv"], "recurse": True}, transformation_ctx="AdditionalFeatures_node1738827123247")

# Script generated for node Control Point
ControlPoint_node1738873910785 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://humanaproject/staging/Control Point.csv"], "recurse": True}, transformation_ctx="ControlPoint_node1738873910785")

# Script generated for node Change Schema
ChangeSchema_node1738874778659 = ApplyMapping.apply(frame=CostUtilization_node1738874585187, mappings=[("nonpar_clm_ct_pmpm", "string", "nonpar_clm_ct_pmpm", "string"), ("nonpar_allowed_pmpm_cost", "string", "nonpar_allowed_pmpm_cost", "string"), ("nonpar_net_paid_pmpm_cost", "string", "nonpar_net_paid_pmpm_cost", "string"), ("nonpar_cob_paid_pmpm_cost", "string", "nonpar_cob_paid_pmpm_cost", "string"), ("nonpar_coins_pmpm_cost", "string", "nonpar_coins_pmpm_cost", "string"), ("nonpar_copay_pmpm_cost", "string", "nonpar_copay_pmpm_cost", "string"), ("nonpar_deduct_pmpm_cost", "string", "nonpar_deduct_pmpm_cost", "string"), ("nonpar_mbr_resp_pmpm_cost", "string", "nonpar_mbr_resp_pmpm_cost", "string"), ("nonpar_ds_clm", "string", "nonpar_ds_clm", "string"), ("oontwk_clm_ct_pmpm", "string", "oontwk_clm_ct_pmpm", "string"), ("oontwk_allowed_pmpm_cost", "string", "oontwk_allowed_pmpm_cost", "string"), ("oontwk_net_paid_pmpm_cost", "string", "oontwk_net_paid_pmpm_cost", "string"), ("oontwk_cob_paid_pmpm_cost", "string", "oontwk_cob_paid_pmpm_cost", "string"), ("oontwk_coins_pmpm_cost", "string", "oontwk_coins_pmpm_cost", "string"), ("oontwk_copay_pmpm_cost", "string", "oontwk_copay_pmpm_cost", "string"), ("oontwk_deduct_pmpm_cost", "string", "oontwk_deduct_pmpm_cost", "string"), ("oontwk_mbr_resp_pmpm_cost", "string", "oontwk_mbr_resp_pmpm_cost", "string"), ("oontwk_ds_clm", "string", "oontwk_ds_clm", "string"), ("total_allowed_pmpm_cost", "string", "total_allowed_pmpm_cost", "string"), ("total_net_paid_pmpm_cost", "string", "total_net_paid_pmpm_cost", "string"), ("total_cob_paid_pmpm_cost", "string", "total_cob_paid_pmpm_cost", "string"), ("total_coins_pmpm_cost", "string", "total_coins_pmpm_cost", "string"), ("total_copay_pmpm_cost", "string", "total_copay_pmpm_cost", "string"), ("total_deduct_pmpm_cost", "string", "total_deduct_pmpm_cost", "string"), ("total_mbr_resp_pmpm_cost", "string", "total_mbr_resp_pmpm_cost", "string"), ("days_since_last_clm", "string", "days_since_last_clm", "string"), ("bh_rtc_admit_ct_pmpm", "string", "bh_rtc_admit_ct_pmpm", "string"), ("bh_rtc_admit_days_pmpm", "string", "bh_rtc_admit_days_pmpm", "string"), ("bh_psyc_visit_ct_pmpm", "string", "bh_psyc_visit_ct_pmpm", "string"), ("total_ip_acute_admit_days_pmpm", "string", "total_ip_acute_admit_days_pmpm", "string"), ("total_ip_ltach_admit_days_pmpm", "string", "total_ip_ltach_admit_days_pmpm", "string"), ("total_ip_maternity_admit_days_pmpm", "string", "total_ip_maternity_admit_days_pmpm", "string"), ("total_ip_mhsa_admit_days_pmpm", "string", "total_ip_mhsa_admit_days_pmpm", "string"), ("total_ip_rehab_admit_days_pmpm", "string", "total_ip_rehab_admit_days_pmpm", "string"), ("total_ip_snf_admit_days_pmpm", "string", "total_ip_snf_admit_days_pmpm", "string"), ("id", "string", "cu_id", "string")], transformation_ctx="ChangeSchema_node1738874778659")

# Script generated for node Change Schema
ChangeSchema_node1738874871429 = ApplyMapping.apply(frame=Demographics_node1738874840681, mappings=[("lang_spoken_cd", "string", "lang_spoken_cd", "string"), ("rucc_category", "string", "rucc_category", "string"), ("riskarr_downside", "string", "riskarr_downside", "string"), ("riskarr_upside", "string", "riskarr_upside", "string"), ("riskarr_rewards", "string", "riskarr_rewards", "string"), ("riskarr_global", "string", "riskarr_global", "string"), ("id", "string", "demo_id", "string")], transformation_ctx="ChangeSchema_node1738874871429")

# Script generated for node Change Schema
ChangeSchema_node1738873718653 = ApplyMapping.apply(frame=target_members_node1738873669735, mappings=[("preventive_visit_gap_ind", "string", "preventive_visit_gap_ind", "string"), ("id", "string", "id", "string")], transformation_ctx="ChangeSchema_node1738873718653")

# Script generated for node Change Schema
ChangeSchema_node1738873828784 = ApplyMapping.apply(frame=AdditionalFeatures_node1738827123247, mappings=[("cms_frailty_ind", "string", "cms_frailty_ind", "string"), ("cms_tot_ma_payment_amt", "string", "cms_tot_ma_payment_amt", "string"), ("cms_tot_partd_payment_amt", "string", "cms_tot_partd_payment_amt", "string"), ("atlas_recfacpth14", "string", "atlas_recfacpth14", "string"), ("atlas_ffrpth14", "string", "atlas_ffrpth14", "string"), ("atlas_fsrpth14", "string", "atlas_fsrpth14", "string"), ("atlas_grocpth14", "string", "atlas_grocpth14", "string"), ("atlas_povertyallagespct", "string", "atlas_povertyallagespct", "string"), ("cci_score", "string", "cci_score", "string"), ("fci_score", "string", "fci_score", "string"), ("dcsi_score", "string", "dcsi_score", "string"), ("id", "string", "Add_feat_id", "string")], transformation_ctx="ChangeSchema_node1738873828784")

# Script generated for node Change Schema
ChangeSchema_node1738873950449 = ApplyMapping.apply(frame=ControlPoint_node1738873910785, mappings=[("cnt_cp_emails_0", "string", "cnt_cp_emails_0", "string"), ("cnt_cp_emails_1", "string", "cnt_cp_emails_1", "string"), ("cnt_cp_emails_2", "string", "cnt_cp_emails_2", "string"), ("cnt_cp_emails_3", "string", "cnt_cp_emails_3", "string"), ("cnt_cp_emails_4", "string", "cnt_cp_emails_4", "string"), ("cnt_cp_emails_5", "string", "cnt_cp_emails_5", "string"), ("cnt_cp_emails_6", "string", "cnt_cp_emails_6", "string"), ("cnt_cp_emails_7", "string", "cnt_cp_emails_7", "string"), ("cnt_cp_emails_8", "string", "cnt_cp_emails_8", "string"), ("cnt_cp_emails_9", "string", "cnt_cp_emails_9", "string"), ("cnt_cp_emails_10", "string", "cnt_cp_emails_10", "string"), ("cnt_cp_emails_11", "string", "cnt_cp_emails_11", "string"), ("cnt_cp_print_0", "string", "cnt_cp_print_0", "string"), ("cnt_cp_print_1", "string", "cnt_cp_print_1", "string"), ("cnt_cp_print_2", "string", "cnt_cp_print_2", "string"), ("cnt_cp_print_3", "string", "cnt_cp_print_3", "string"), ("cnt_cp_print_4", "string", "cnt_cp_print_4", "string"), ("cnt_cp_print_5", "string", "cnt_cp_print_5", "string"), ("cnt_cp_print_6", "string", "cnt_cp_print_6", "string"), ("cnt_cp_print_7", "string", "cnt_cp_print_7", "string"), ("cnt_cp_print_8", "string", "cnt_cp_print_8", "string"), ("cnt_cp_print_9", "string", "cnt_cp_print_9", "string"), ("cnt_cp_print_10", "string", "cnt_cp_print_10", "string"), ("cnt_cp_print_11", "string", "cnt_cp_print_11", "string"), ("cnt_cp_vat_0", "string", "cnt_cp_vat_0", "string"), ("cnt_cp_vat_1", "string", "cnt_cp_vat_1", "string"), ("cnt_cp_vat_2", "string", "cnt_cp_vat_2", "string"), ("cnt_cp_vat_3", "string", "cnt_cp_vat_3", "string"), ("cnt_cp_vat_4", "string", "cnt_cp_vat_4", "string"), ("cnt_cp_vat_5", "string", "cnt_cp_vat_5", "string"), ("cnt_cp_vat_6", "string", "cnt_cp_vat_6", "string"), ("cnt_cp_vat_7", "string", "cnt_cp_vat_7", "string"), ("cnt_cp_vat_8", "string", "cnt_cp_vat_8", "string"), ("cnt_cp_vat_9", "string", "cnt_cp_vat_9", "string"), ("cnt_cp_vat_10", "string", "cnt_cp_vat_10", "string"), ("cnt_cp_vat_11", "string", "cnt_cp_vat_11", "string"), ("cnt_cp_webstatement_0", "string", "cnt_cp_webstatement_0", "string"), ("cnt_cp_webstatement_1", "string", "cnt_cp_webstatement_1", "string"), ("cnt_cp_webstatement_2", "string", "cnt_cp_webstatement_2", "string"), ("cnt_cp_webstatement_3", "string", "cnt_cp_webstatement_3", "string"), ("cnt_cp_webstatement_4", "string", "cnt_cp_webstatement_4", "string"), ("cnt_cp_webstatement_5", "string", "cnt_cp_webstatement_5", "string"), ("cnt_cp_webstatement_6", "string", "cnt_cp_webstatement_6", "string"), ("cnt_cp_webstatement_7", "string", "cnt_cp_webstatement_7", "string"), ("cnt_cp_webstatement_8", "string", "cnt_cp_webstatement_8", "string"), ("cnt_cp_webstatement_9", "string", "cnt_cp_webstatement_9", "string"), ("cnt_cp_webstatement_10", "string", "cnt_cp_webstatement_10", "string"), ("cnt_cp_webstatement_11", "string", "cnt_cp_webstatement_11", "string"), ("cnt_cp_livecall_0", "string", "cnt_cp_livecall_0", "string"), ("cnt_cp_livecall_1", "string", "cnt_cp_livecall_1", "string"), ("cnt_cp_livecall_2", "string", "cnt_cp_livecall_2", "string"), ("cnt_cp_livecall_3", "string", "cnt_cp_livecall_3", "string"), ("cnt_cp_livecall_4", "string", "cnt_cp_livecall_4", "string"), ("cnt_cp_livecall_5", "string", "cnt_cp_livecall_5", "string"), ("cnt_cp_livecall_6", "string", "cnt_cp_livecall_6", "string"), ("cnt_cp_livecall_7", "string", "cnt_cp_livecall_7", "string"), ("cnt_cp_livecall_8", "string", "cnt_cp_livecall_8", "string"), ("cnt_cp_livecall_9", "string", "cnt_cp_livecall_9", "string"), ("cnt_cp_livecall_10", "string", "cnt_cp_livecall_10", "string"), ("cnt_cp_livecall_11", "string", "cnt_cp_livecall_11", "string"), ("cnt_cp_emails_pmpm_ct", "string", "cnt_cp_emails_pmpm_ct", "string"), ("cnt_cp_print_pmpm_ct", "string", "cnt_cp_print_pmpm_ct", "string"), ("cnt_cp_vat_pmpm_ct", "string", "cnt_cp_vat_pmpm_ct", "string"), ("cnt_cp_webstatement_pmpm_ct", "string", "cnt_cp_webstatement_pmpm_ct", "string"), ("cnt_cp_livecall_pmpm_ct", "string", "cnt_cp_livecall_pmpm_ct", "string"), ("id", "string", "cp_id", "string")], transformation_ctx="ChangeSchema_node1738873950449")

# Script generated for node Custom Transform
CustomTransform_node1738875101143 = MyTransform(glueContext, DynamicFrameCollection({"ChangeSchema_node1738874871429": ChangeSchema_node1738874871429}, glueContext))

# Script generated for node Join
ChangeSchema_node1738873718653DF = ChangeSchema_node1738873718653.toDF()
ChangeSchema_node1738873828784DF = ChangeSchema_node1738873828784.toDF()
Join_node1738873869640 = DynamicFrame.fromDF(ChangeSchema_node1738873718653DF.join(ChangeSchema_node1738873828784DF, (ChangeSchema_node1738873718653DF['id'] == ChangeSchema_node1738873828784DF['Add_feat_id']), "left"), glueContext, "Join_node1738873869640")

# Script generated for node Join
Join_node1738873869640DF = Join_node1738873869640.toDF()
ChangeSchema_node1738873950449DF = ChangeSchema_node1738873950449.toDF()
Join_node1738873975562 = DynamicFrame.fromDF(Join_node1738873869640DF.join(ChangeSchema_node1738873950449DF, (Join_node1738873869640DF['id'] == ChangeSchema_node1738873950449DF['cp_id']), "left"), glueContext, "Join_node1738873975562")

# Script generated for node Join
Join_node1738873975562DF = Join_node1738873975562.toDF()
ChangeSchema_node1738874778659DF = ChangeSchema_node1738874778659.toDF()
Join_node1738874796833 = DynamicFrame.fromDF(Join_node1738873975562DF.join(ChangeSchema_node1738874778659DF, (Join_node1738873975562DF['id'] == ChangeSchema_node1738874778659DF['cu_id']), "left"), glueContext, "Join_node1738874796833")

job.commit()