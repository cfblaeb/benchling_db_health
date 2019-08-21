from django.db import models


class AcCompoundIdentificationAndMassCheck(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    sample_id = models.CharField(max_length=999, blank=True, null=True)
    rt_min = models.CharField(max_length=999, blank=True, null=True)
    fraction = models.CharField(max_length=999, blank=True, null=True)
    uv_max = models.FloatField(blank=True, null=True)
    uv_absorbance = models.CharField(max_length=999, blank=True, null=True)
    uv_spectrum = models.CharField(max_length=999, blank=True, null=True)
    mz_pos = models.FloatField(blank=True, null=True)
    predicted_formula_pos = models.CharField(max_length=999, blank=True, null=True)
    adducts_pos = models.CharField(max_length=999, blank=True, null=True)
    msms_pos = models.FloatField(blank=True, null=True)
    msms_spectrum_pos = models.CharField(max_length=999, blank=True, null=True)
    mz_neg = models.FloatField(blank=True, null=True)
    predicted_formula_neg = models.CharField(max_length=999, blank=True, null=True)
    adducts_neg = models.CharField(max_length=999, blank=True, null=True)
    msms_neg = models.FloatField(blank=True, null=True)
    msms_spectrum_neg = models.CharField(max_length=999, blank=True, null=True)
    dictionary_hit_dnp = models.CharField(max_length=999, blank=True, null=True)
    dnp_report = models.CharField(max_length=999, blank=True, null=True)
    antibase_hit = models.CharField(max_length=999, blank=True, null=True)
    antibase_report = models.CharField(max_length=999, blank=True, null=True)
    streptomedb_hit = models.CharField(max_length=999, blank=True, null=True)
    streptomedb_report = models.CharField(max_length=999, blank=True, null=True)
    reported_activity = models.CharField(max_length=999, blank=True, null=True)
    identity = models.CharField(max_length=999, blank=True, null=True)
    result_image = models.TextField(blank=True, null=True)
    result_file = models.TextField(blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_compound_identification_and_mass_check'


class AcCompoundQuantificationResult(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    sample = models.CharField(max_length=999, blank=True, null=True)
    injection_number = models.IntegerField(blank=True, null=True)
    compound = models.CharField(max_length=999, blank=True, null=True)
    concentration = models.FloatField(blank=True, null=True)
    concentration_unit = models.CharField(max_length=999, blank=True, null=True)
    dilution_factor = models.FloatField(blank=True, null=True)
    injection_volume = models.FloatField(blank=True, null=True)
    injection_volume_unit = models.CharField(max_length=999, blank=True, null=True)
    acquisition_time = models.DateTimeField(blank=True, null=True)
    acquisition_method_name = models.CharField(max_length=999, blank=True, null=True)
    processing_method_name = models.CharField(max_length=999, blank=True, null=True)
    assay_run = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_compound_quantification_result'


class AcCompoundQuantificationResultMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_compound_quantification_result_multi'


class AcCompoundQuantificationSummaryResult(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    sample = models.CharField(max_length=999, blank=True, null=True)
    compound = models.CharField(max_length=999, blank=True, null=True)
    concentration = models.FloatField(blank=True, null=True)
    concentration_unit = models.CharField(max_length=999, blank=True, null=True)
    dilution_factor = models.FloatField(blank=True, null=True)
    acquisition_method_name = models.CharField(max_length=999, blank=True, null=True)
    processing_method_name = models.CharField(max_length=999, blank=True, null=True)
    assay_run = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_compound_quantification_summary_result'


class AcCompoundQuantificationSummaryResultMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_compound_quantification_summary_result_multi'


class AcFluxomics(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    status_field = models.CharField(db_column='status$', max_length=999, blank=True, null=True)
    display_id_field = models.CharField(db_column='display_id$', max_length=999, blank=True, null=True)
    url_field = models.CharField(db_column='url$', max_length=999, blank=True, null=True)
    scheduled_on_field = models.DateField(db_column='scheduled_on$', blank=True, null=True)
    budget = models.CharField(max_length=999, blank=True, null=True)
    expected_delivery_date = models.DateField(blank=True, null=True)
    expected_number_of_samples = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)
    comments_fulfiller = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_fluxomics'


class AcGlycanAnalysis(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    status_field = models.CharField(db_column='status$', max_length=999, blank=True, null=True)
    display_id_field = models.CharField(db_column='display_id$', max_length=999, blank=True, null=True)
    url_field = models.CharField(db_column='url$', max_length=999, blank=True, null=True)
    scheduled_on_field = models.DateField(db_column='scheduled_on$', blank=True, null=True)
    budget = models.CharField(max_length=999, blank=True, null=True)
    expected_delivery_date = models.DateField(blank=True, null=True)
    expected_number_of_samples = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)
    comments_fulfiller = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_glycan_analysis'


class AcGlycanAnalysisResult(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    sample = models.CharField(max_length=999, blank=True, null=True)
    annotation = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    additional_attachments = models.TextField(blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_glycan_analysis_result'


class AcGlycanAnalysisResultMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_glycan_analysis_result_multi'


class AcMethodDevelopment(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    status_field = models.CharField(db_column='status$', max_length=999, blank=True, null=True)
    display_id_field = models.CharField(db_column='display_id$', max_length=999, blank=True, null=True)
    url_field = models.CharField(db_column='url$', max_length=999, blank=True, null=True)
    scheduled_on_field = models.DateField(db_column='scheduled_on$', blank=True, null=True)
    budget = models.CharField(max_length=999, blank=True, null=True)
    analysis = models.CharField(max_length=999, blank=True, null=True)
    standards_available = models.CharField(max_length=999, blank=True, null=True)
    expected_number_of_samples = models.IntegerField(blank=True, null=True)
    planned_start_date = models.DateField(blank=True, null=True)
    planned_end_date = models.DateField(blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)
    comments_fulfiller = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_method_development'


class AcProteomics(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    status_field = models.CharField(db_column='status$', max_length=999, blank=True, null=True)
    display_id_field = models.CharField(db_column='display_id$', max_length=999, blank=True, null=True)
    url_field = models.CharField(db_column='url$', max_length=999, blank=True, null=True)
    scheduled_on_field = models.DateField(db_column='scheduled_on$', blank=True, null=True)
    budget = models.CharField(max_length=999, blank=True, null=True)
    expected_delivery_date = models.DateField(blank=True, null=True)
    expected_number_of_samples = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)
    comments_fulfiller = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_proteomics'


class AcTargetedMetabolomics(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    status_field = models.CharField(db_column='status$', max_length=999, blank=True, null=True)
    display_id_field = models.CharField(db_column='display_id$', max_length=999, blank=True, null=True)
    url_field = models.CharField(db_column='url$', max_length=999, blank=True, null=True)
    scheduled_on_field = models.DateField(db_column='scheduled_on$', blank=True, null=True)
    budget = models.CharField(max_length=999, blank=True, null=True)
    expected_delivery_date = models.DateField(blank=True, null=True)
    expected_number_of_samples = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)
    comments_fulfiller = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_targeted_metabolomics'


class AcTargetedProteomicsResult(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    sample = models.CharField(max_length=999, blank=True, null=True)
    # This field type is a guess.
    result_file = models.TextField(blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_targeted_proteomics_result'


class AcUntargetedMetabolomics(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    status_field = models.CharField(db_column='status$', max_length=999, blank=True, null=True)
    display_id_field = models.CharField(db_column='display_id$', max_length=999, blank=True, null=True)
    url_field = models.CharField(db_column='url$', max_length=999, blank=True, null=True)
    scheduled_on_field = models.DateField(db_column='scheduled_on$', blank=True, null=True)
    budget = models.CharField(max_length=999, blank=True, null=True)
    expected_delivery_date = models.DateField(blank=True, null=True)
    expected_number_of_samples = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)
    comments_fulfiller = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ac_untargeted_metabolomics'


class AssayRecordStatus(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    record_id = models.CharField(max_length=999, blank=True, null=True)
    is_reviewed = models.BooleanField(blank=True, null=True)
    validation_status = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'assay_record_status'


class AssayResultSchema(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    schema_type = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    parent_schema_id = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'assay_result_schema'


class AssayRunSchema(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    schema_type = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    parent_schema_id = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'assay_run_schema'


class Author(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    user_id = models.CharField(max_length=999, blank=True, null=True)
    entry_id = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'author'


class Batch(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    creator_id = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    entity_id = models.CharField(max_length=999, blank=True, null=True)
    concentration_si = models.FloatField(blank=True, null=True)
    concentration_display_units = models.CharField(max_length=999, blank=True, null=True)
    url = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'batch'


class BatchSchema(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    schema_type = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    registry_id = models.CharField(max_length=999, blank=True, null=True)
    entity_schema_id = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'batch_schema'


class BiochemistryAnalyzerYsiIpc(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    duration = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'biochemistry_analyzer_ysi_ipc'


class Box(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    creator_id = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    barcode = models.CharField(max_length=999, blank=True, null=True)
    url = models.CharField(max_length=999, blank=True, null=True)
    location_id = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'box'


class BoxSchema(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    schema_type = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    registry_id = models.CharField(max_length=999, blank=True, null=True)
    prefix = models.CharField(max_length=999, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    container_schema_id = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'box_schema'


class CellLineKosV1(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    ko_grna = models.CharField(max_length=999, blank=True, null=True)
    no_reads = models.IntegerField(blank=True, null=True)
    size = models.CharField(max_length=999, blank=True, null=True)
    perc_fraction = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cell_line_kos_v1'


class CellLineKosV1Multi(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cell_line_kos_v1_multi'


class CellPurchasingDescription(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    catalog_number = models.CharField(max_length=999, blank=True, null=True)
    origin_description = models.CharField(max_length=999, blank=True, null=True)
    origin_gender = models.CharField(max_length=999, blank=True, null=True)
    origin_disease = models.CharField(max_length=999, blank=True, null=True)
    biosafety_level = models.CharField(max_length=999, blank=True, null=True)
    morphology = models.CharField(max_length=999, blank=True, null=True)
    culture_medium = models.CharField(max_length=999, blank=True, null=True)
    split_ratio = models.FloatField(blank=True, null=True)
    incubation_consditions = models.CharField(max_length=999, blank=True, null=True)
    doubling_time = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cell_purchasing_description'


class ChoCampaignTransfectionStatus(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    design = models.CharField(max_length=999, blank=True, null=True)
    campaign_id = models.CharField(max_length=999, blank=True, null=True)
    transfection = models.IntegerField(blank=True, null=True)
    ok = models.CharField(max_length=999, blank=True, null=True)
    comment = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cho_campaign_transfection_status'


class ChoCampaignTransfectionStatusMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cho_campaign_transfection_status_multi'


class ChoCellLineKos(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    campaign_id = models.CharField(max_length=999, blank=True, null=True)
    grna = models.CharField(max_length=999, blank=True, null=True)
    number_reads = models.IntegerField(blank=True, null=True)
    size = models.CharField(max_length=999, blank=True, null=True)
    per_fraction = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cho_cell_line_kos'


class ChoCellLineKosMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cho_cell_line_kos_multi'


class ChoCellLineSelection(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    cho_cell_line = models.CharField(max_length=999, blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)
    medium = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cho_cell_line_selection'


class ChoCellLineSelectionMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cho_cell_line_selection_multi'


class ChoIndelV1(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    grna = models.CharField(max_length=999, blank=True, null=True)
    size = models.CharField(max_length=999, blank=True, null=True)
    perc_fraction = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cho_indel_v1'


class ChoIndelV1Multi(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cho_indel_v1_multi'


class ChoIndelV2(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    verification_round = models.CharField(max_length=999, blank=True, null=True)
    grna = models.CharField(max_length=999, blank=True, null=True)
    perc_fraction = models.CharField(max_length=999, blank=True, null=True)
    size = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cho_indel_v2'


class ChoIndelV2Multi(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cho_indel_v2_multi'


class Comment(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    record_id = models.CharField(max_length=999, blank=True, null=True)
    creator_id = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=999, blank=True, null=True)
    validation_status = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'comment'


class CompoundId(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'compound_id'


class Container(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    creator_id = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    barcode = models.CharField(max_length=999, blank=True, null=True)
    url = models.CharField(max_length=999, blank=True, null=True)
    box_id = models.CharField(max_length=999, blank=True, null=True)
    location_id = models.CharField(max_length=999, blank=True, null=True)
    plate_id = models.CharField(max_length=999, blank=True, null=True)
    row_index = models.IntegerField(blank=True, null=True)
    column_index = models.IntegerField(blank=True, null=True)
    volume_si = models.FloatField(blank=True, null=True)
    volume_display_units = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'container'


class ContainerBatch(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    batch_id = models.CharField(max_length=999, blank=True, null=True)
    container_id = models.CharField(max_length=999, blank=True, null=True)
    entity_id = models.CharField(max_length=999, blank=True, null=True)
    concentration_si = models.FloatField(blank=True, null=True)
    concentration_display_units = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'container_batch'


class ContainerContent(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    batch_id = models.CharField(max_length=999, blank=True, null=True)
    container_id = models.CharField(max_length=999, blank=True, null=True)
    entity_id = models.CharField(max_length=999, blank=True, null=True)
    concentration_si = models.FloatField(blank=True, null=True)
    concentration_display_units = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'container_content'


class ContainerSchema(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    schema_type = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    registry_id = models.CharField(max_length=999, blank=True, null=True)
    prefix = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'container_schema'


class ContainerTransfer(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    input_batch_id = models.CharField(max_length=999, blank=True, null=True)
    input_container_id = models.CharField(max_length=999, blank=True, null=True)
    input_entity_id = models.CharField(max_length=999, blank=True, null=True)
    output_container_id = models.CharField(max_length=999, blank=True, null=True)
    volume_si = models.FloatField(blank=True, null=True)
    volume_display_units = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'container_transfer'


class DataTableRecord(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    assay_run_id = models.CharField(max_length=999, blank=True, null=True)
    assay_result_id = models.CharField(max_length=999, blank=True, null=True)
    batch_id = models.CharField(max_length=999, blank=True, null=True)
    entry_id = models.CharField(max_length=999, blank=True, null=True)
    stage_run_id = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'data_table_record'


class EntitySchema(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    schema_type = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    entity_type = models.CharField(max_length=999, blank=True, null=True)
    registry_id = models.CharField(max_length=999, blank=True, null=True)
    prefix = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'entity_schema'


class Entry(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    display_id = models.CharField(max_length=999, blank=True, null=True)
    folder_id = models.CharField(max_length=999, blank=True, null=True)
    workflow_id = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    review_status = models.CharField(max_length=999, blank=True, null=True)
    review_requested_at = models.DateTimeField(blank=True, null=True)
    review_status_changed_at = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'entry'


class EntryAuditor(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    user_id = models.CharField(max_length=999, blank=True, null=True)
    entry_id = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'entry_auditor'


class Field(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    field_name = models.CharField(max_length=999, blank=True, null=True)
    field_definition_id = models.CharField(max_length=999, blank=True, null=True)
    schema_field_id = models.CharField(max_length=999, blank=True, null=True)
    batch_id = models.CharField(max_length=999, blank=True, null=True)
    box_id = models.CharField(max_length=999, blank=True, null=True)
    container_id = models.CharField(max_length=999, blank=True, null=True)
    location_id = models.CharField(max_length=999, blank=True, null=True)
    plate_id = models.CharField(max_length=999, blank=True, null=True)
    registry_entity_id = models.CharField(max_length=999, blank=True, null=True)
    entry_id = models.CharField(max_length=999, blank=True, null=True)
    result_id = models.CharField(max_length=999, blank=True, null=True)
    run_id = models.CharField(max_length=999, blank=True, null=True)
    request_id = models.CharField(max_length=999, blank=True, null=True)
    request_task_id = models.CharField(max_length=999, blank=True, null=True)
    value_index = models.IntegerField(blank=True, null=True)
    display_value = models.CharField(max_length=999, blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    # This field type is a guess.
    blob_value = models.TextField(blank=True, null=True)
    bool_value = models.BooleanField(blank=True, null=True)
    float_value = models.FloatField(blank=True, null=True)
    date_value = models.DateField(blank=True, null=True)
    datetime_value = models.DateTimeField(blank=True, null=True)
    integer_value = models.IntegerField(blank=True, null=True)
    # This field type is a guess.
    json_value = models.TextField(blank=True, null=True)
    linked_batch_id = models.CharField(max_length=999, blank=True, null=True)
    linked_registry_entity_id = models.CharField(max_length=999, blank=True, null=True)
    linked_entry_id = models.CharField(max_length=999, blank=True, null=True)
    linked_run_id = models.CharField(max_length=999, blank=True, null=True)
    linked_result_id = models.CharField(max_length=999, blank=True, null=True)
    linked_container_id = models.CharField(max_length=999, blank=True, null=True)
    linked_location_id = models.CharField(max_length=999, blank=True, null=True)
    linked_plate_id = models.CharField(max_length=999, blank=True, null=True)
    linked_box_id = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'field'


class FieldDefinition(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    display_name = models.CharField(max_length=999, blank=True, null=True)
    numeric_min = models.FloatField(blank=True, null=True)
    numeric_max = models.FloatField(blank=True, null=True)
    is_multi = models.BooleanField(blank=True, null=True)
    is_required = models.BooleanField(blank=True, null=True)
    dropdown_id = models.CharField(max_length=999, blank=True, null=True)
    target_schema_id = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'field_definition'


class FluxIntracellularMetabolites(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'flux_intracellular_metabolites'


class Folder(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    parent_folder_id = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'folder'


class GcmsTargetedV1(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    compound = models.CharField(max_length=999, blank=True, null=True)
    conc = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=999, blank=True, null=True)
    dilution = models.CharField(max_length=999, blank=True, null=True)
    internal_standard = models.CharField(max_length=999, blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'gcms_targeted_v1'


class GcmsTargetedV1Multi(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'gcms_targeted_v1_multi'


class GrowthRatesAle(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    flask = models.CharField(max_length=999, blank=True, null=True)
    time = models.CharField(max_length=999, blank=True, null=True)
    growth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'growth_rates_ale'


class GrowthRatesAleMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'growth_rates_ale_multi'


class InDevelopmentAnalyticalChemistry(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    status_field = models.CharField(db_column='status$', max_length=999, blank=True, null=True)
    display_id_field = models.CharField(db_column='display_id$', max_length=999, blank=True, null=True)
    url_field = models.CharField(db_column='url$', max_length=999, blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)
    dilution_factor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'in_development_analytical_chemistry'


class IndelOutput(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    grna = models.CharField(max_length=999, blank=True, null=True)
    size = models.CharField(max_length=999, blank=True, null=True)
    per_fraction = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'indel_output'


class IndelOutputMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'indel_output_multi'


class LcmsTargetedMetabolomics(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    batch = models.CharField(max_length=999, blank=True, null=True)
    compound = models.CharField(max_length=999, blank=True, null=True)
    concentration = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'lcms_targeted_metabolomics'


class LcmsTargetedMetabolomicsMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'lcms_targeted_metabolomics_multi'


class Location(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    creator_id = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    barcode = models.CharField(max_length=999, blank=True, null=True)
    location_id = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'location'


class LocationSchema(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    schema_type = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    registry_id = models.CharField(max_length=999, blank=True, null=True)
    prefix = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'location_schema'


class MediaCompositions(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'media_compositions'


class MediaCompositionsMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'media_compositions_multi'


class MediumCompositionIngredient(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    medium = models.CharField(max_length=999, blank=True, null=True)
    ingredient = models.CharField(max_length=999, blank=True, null=True)
    concentration = models.FloatField(blank=True, null=True)
    concentration_unit = models.CharField(max_length=999, blank=True, null=True)
    step = models.CharField(max_length=999, blank=True, null=True)
    assay_run = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'medium_composition_ingredient'


class MediumCompositionIngredientMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'medium_composition_ingredient_multi'


class NbcChemicalAnalysis(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    wt_ev = models.CharField(max_length=999, blank=True, null=True)
    extraction_date = models.DateTimeField(blank=True, null=True)
    no_plates = models.IntegerField(blank=True, null=True)
    plate_sample_collection = models.CharField(max_length=999, blank=True, null=True)
    extraction_solvents = models.CharField(max_length=999, blank=True, null=True)
    three_x_extraction_rpm = models.FloatField(blank=True, null=True)
    three_x_extraction_time = models.FloatField(blank=True, null=True)
    ch2cl2_bioactivity = models.CharField(max_length=999, blank=True, null=True)
    meoh_bioactivity = models.CharField(max_length=999, blank=True, null=True)
    extraction_comments = models.CharField(max_length=999, blank=True, null=True)
    precolumn_purification = models.CharField(max_length=999, blank=True, null=True)
    first_separation_hplc_column = models.CharField(max_length=999, blank=True, null=True)
    first_separation_mobile_phase_composition = models.CharField(max_length=999, blank=True, null=True)
    first_separation_hplc_method = models.CharField(max_length=999, blank=True, null=True)
    first_separation_flow_rate = models.FloatField(blank=True, null=True)
    first_separation_run_time = models.FloatField(blank=True, null=True)
    first_separation_fraction_bioactivity = models.CharField(max_length=999, blank=True, null=True)
    first_separation_comments = models.CharField(max_length=999, blank=True, null=True)
    second_separation_hplc_column = models.CharField(max_length=999, blank=True, null=True)
    second_separation_mobile_phase_composition = models.CharField(max_length=999, blank=True, null=True)
    second_separation_hplc_method = models.CharField(max_length=999, blank=True, null=True)
    second_separation_flow_rate = models.FloatField(blank=True, null=True)
    second_separation_run_time = models.FloatField(blank=True, null=True)
    second_separation_fraction_bioactivity = models.CharField(max_length=999, blank=True, null=True)
    second_separation_comments = models.CharField(max_length=999, blank=True, null=True)
    third_separation_hplc_column = models.CharField(max_length=999, blank=True, null=True)
    third_separation_mobile_phase_composition = models.CharField(max_length=999, blank=True, null=True)
    third_separation_hplc_method = models.CharField(max_length=999, blank=True, null=True)
    third_separation_flow_rate = models.FloatField(blank=True, null=True)
    third_separation_run_time = models.FloatField(blank=True, null=True)
    third_separation_fraction_bioactivity = models.CharField(max_length=999, blank=True, null=True)
    third_separation_comments = models.CharField(max_length=999, blank=True, null=True)
    id_molecule = models.CharField(max_length=999, blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'nbc_chemical_analysis'


class NbcChemicalAnalysisMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'nbc_chemical_analysis_multi'


class NbcCoAleStatus(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    strain = models.CharField(max_length=999, blank=True, null=True)
    round = models.IntegerField(blank=True, null=True)
    stage_1_date = models.DateField(blank=True, null=True)
    stage_1_comment = models.CharField(max_length=999, blank=True, null=True)
    stage_2_date = models.CharField(max_length=999, blank=True, null=True)
    stage_2_comment = models.CharField(max_length=999, blank=True, null=True)
    halo_size = models.CharField(max_length=999, blank=True, null=True)
    stage_3_date = models.DateField(blank=True, null=True)
    stage_3_comment = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'nbc_co_ale_status'


class NbcEvolvedStrain(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    evo_cycle_halo = models.IntegerField(blank=True, null=True)
    halo_size_post_growth = models.CharField(max_length=999, blank=True, null=True)
    halo_size_on_isp2 = models.CharField(max_length=999, blank=True, null=True)
    halo_still_present = models.CharField(max_length=999, blank=True, null=True)
    plan_of_action = models.CharField(max_length=999, blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)
    # This field type is a guess.
    plate_image_before_freezing = models.TextField(blank=True, null=True)
    # This field type is a guess.
    frozen_stock_image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'nbc_evolved_strain'


class NbcEvolvedStrainMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'nbc_evolved_strain_multi'


class NbcIdentifiedBioactiveCompounds(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    wt_ev = models.CharField(max_length=999, blank=True, null=True)
    identified_bioactive_compounds = models.CharField(max_length=999, blank=True, null=True)
    hplc_column = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'nbc_identified_bioactive_compounds'


class NbcStrain(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    colony_color = models.CharField(max_length=999, blank=True, null=True)
    colony_morphology = models.CharField(max_length=999, blank=True, null=True)
    wt_halo_ab = models.CharField(max_length=999, blank=True, null=True)
    wt_halo_ecoli = models.CharField(max_length=999, blank=True, null=True)
    automated_ale = models.CharField(max_length=999, blank=True, null=True)
    # This field type is a guess.
    plate_image_before_freezing = models.TextField(blank=True, null=True)
    nbc_wgs = models.CharField(max_length=999, blank=True, null=True)
    medina_medium = models.CharField(max_length=999, blank=True, null=True)
    medina_fermentation_time = models.IntegerField(blank=True, null=True)
    medina_biological_assay = models.CharField(max_length=999, blank=True, null=True)
    medina_compounds = models.CharField(max_length=999, blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'nbc_strain'


class NbcStrainMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'nbc_strain_multi'


class NonQuantitativeResultsByMassSpectrometry(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    sample_id = models.CharField(max_length=999, blank=True, null=True)
    # This field type is a guess.
    file = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'non_quantitative_results_by_mass_spectrometry'


class Plate(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    creator_id = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    barcode = models.CharField(max_length=999, blank=True, null=True)
    url = models.CharField(max_length=999, blank=True, null=True)
    location_id = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'plate'


class PlateSchema(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    schema_type = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    registry_id = models.CharField(max_length=999, blank=True, null=True)
    prefix = models.CharField(max_length=999, blank=True, null=True)
    plate_type = models.CharField(max_length=999, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    container_schema_id = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'plate_schema'


class Project(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'project'


class QuantificationRun(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    run_name = models.CharField(max_length=999, blank=True, null=True)
    run_date = models.DateField(blank=True, null=True)
    instrument_name = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantification_run'


class QuantificationRunMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantification_run_multi'


class QuantificationSummaryRun(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantification_summary_run'


class QuantificationSummaryRunMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantification_summary_run_multi'


class QuantifyAminoAcids(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    instrument = models.CharField(max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_amino_acids'


class QuantifyAminoAcidsMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_amino_acids_multi'


class QuantifyAnionicAndAromaticMetabolites(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_anionic_and_aromatic_metabolites'


class QuantifyAntibiotics(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_antibiotics'


class QuantifyAntibioticsMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_antibiotics_multi'


class QuantifyAromaticCompounds(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_aromatic_compounds'


class QuantifyFattyAcidsFa(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_fatty_acids_fa'


class QuantifyFattyAcidsMethylEstersFame(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_fatty_acids_methyl_esters_fame'


class QuantifyGibberellins(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_gibberellins'


class QuantifyGibberellinsMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_gibberellins_multi'


class QuantifyHmpIntermediates(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    instrument = models.CharField(max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_hmp_intermediates'


class QuantifyHmpIntermediatesMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_hmp_intermediates_multi'


class QuantifyLactones(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_lactones'


class QuantifyMethylTransferases(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_methyl_transferases'


class QuantifyMethylTransferasesMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_methyl_transferases_multi'


class QuantifyMiaPathwayIntermediates(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_mia_pathway_intermediates'


class QuantifyMiaPathwayIntermediatesMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_mia_pathway_intermediates_multi'


class QuantifyNads(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_nads'


class QuantifyNadsMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_nads_multi'


class QuantifyOrganicAcids(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_organic_acids'


class QuantifyOrganicAcidsAc(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_organic_acids_ac'


class QuantifyOrganicAcidsAcMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_organic_acids_ac_multi'


class QuantifyOrganicAcidsMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_organic_acids_multi'


class QuantifyRosmarinicAcid(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_rosmarinic_acid'


class QuantifyRosmarinicAcidMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_rosmarinic_acid_multi'


class QuantifySerineIntermediates(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_serine_intermediates'


class QuantifySerineIntermediatesMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_serine_intermediates_multi'


class QuantifySugars(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_sugars'


class QuantifyTcaCycleIntermediates(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_tca_cycle_intermediates'


class QuantifyTcaCycleIntermediatesMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_tca_cycle_intermediates_multi'


class QuantifyTransporterCompounds(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    # This field type is a guess.
    analytes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_transporter_compounds'


class QuantifyTransporterCompoundsMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_transporter_compounds_multi'


class QuantifyVolatileOrganicCompoundsVoc(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)
    instrument = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'quantify_volatile_organic_compounds_voc'


class RegistryEntity(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    file_registry_id = models.CharField(max_length=999, blank=True, null=True)
    creator_id = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    folder_id = models.CharField(max_length=999, blank=True, null=True)
    project_id = models.CharField(max_length=999, blank=True, null=True)
    url = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    validation_status = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'registry_entity'


class RequestAssignee(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id = models.CharField(max_length=999, blank=True, null=True)
    user_id = models.CharField(max_length=999, blank=True, null=True)
    team_id = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'request_assignee'


class RequestFulfillment(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    request_id = models.CharField(max_length=999, blank=True, null=True)
    sample_group_id = models.CharField(max_length=999, blank=True, null=True)
    request_task_id = models.CharField(max_length=999, blank=True, null=True)
    entry_id = models.CharField(max_length=999, blank=True, null=True)
    workflow_id = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'request_fulfillment'


class RequestSample(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id = models.CharField(max_length=999, blank=True, null=True)
    sample_group_id = models.CharField(max_length=999, blank=True, null=True)
    batch_id = models.CharField(max_length=999, blank=True, null=True)
    entity_id = models.CharField(max_length=999, blank=True, null=True)
    container_id = models.CharField(max_length=999, blank=True, null=True)
    field_name = models.CharField(max_length=999, blank=True, null=True)
    row_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'request_sample'


class RequestSchema(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    schema_type = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    parent_schema_id = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'request_schema'


class ResequencingAle(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    isolate = models.CharField(max_length=999, blank=True, null=True)
    read_files_text = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'resequencing_ale'


class ResequencingAleMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'resequencing_ale_multi'


class SawtoothAle(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    time = models.CharField(max_length=999, blank=True, null=True)
    od = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'sawtooth_ale'


class SawtoothAleMulti(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    from_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'sawtooth_ale_multi'


class Schema(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    schema_type = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'schema'


class SchemaField(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    schema_id = models.CharField(max_length=999, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)
    display_name = models.CharField(max_length=999, blank=True, null=True)
    numeric_min = models.FloatField(blank=True, null=True)
    numeric_max = models.FloatField(blank=True, null=True)
    is_multi = models.BooleanField(blank=True, null=True)
    is_required = models.BooleanField(blank=True, null=True)
    selector_id = models.CharField(max_length=999, blank=True, null=True)
    target_schema_id = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'schema_field'


class StageRun(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    stage_name = models.CharField(max_length=999, blank=True, null=True)
    entry_id = models.CharField(max_length=999, blank=True, null=True)
    workflow_id = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=999, blank=True, null=True)
    # This field type is a guess.
    exp_condition_values = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'stage_run'


class StageRunSample(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    stage_run_id = models.CharField(max_length=999, blank=True, null=True)
    batch_id = models.CharField(max_length=999, blank=True, null=True)
    entity_id = models.CharField(max_length=999, blank=True, null=True)
    type = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'stage_run_sample'


class StrainValidation(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    name_antibiotic_1 = models.CharField(max_length=999, blank=True, null=True)
    growth_antibiotic_1 = models.CharField(max_length=999, blank=True, null=True)
    name_antibiotic_2 = models.CharField(max_length=999, blank=True, null=True)
    growth_antibiotic_2 = models.CharField(max_length=999, blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'strain_validation'


class Team(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    description = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'team'


class TeamMember(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    team_id = models.CharField(max_length=999, blank=True, null=True)
    user_id = models.CharField(max_length=999, blank=True, null=True)
    role = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'team_member'


class UntargetedInstrumentParameters(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    solvents = models.CharField(max_length=999, blank=True, null=True)
    parameter = models.CharField(max_length=999, blank=True, null=True)
    description = models.CharField(max_length=999, blank=True, null=True)
    temperature = models.CharField(max_length=999, blank=True, null=True)
    volume = models.CharField(max_length=999, blank=True, null=True)
    dad = models.CharField(max_length=999, blank=True, null=True)
    polarity = models.CharField(max_length=999, blank=True, null=True)
    scan_range = models.CharField(max_length=999, blank=True, null=True)
    fragmentation = models.CharField(max_length=999, blank=True, null=True)
    # This field type is a guess.
    report = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'untargeted_instrument_parameters'


class User(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    handle = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    email = models.CharField(max_length=999, blank=True, null=True)
    is_suspended = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'user'


class ValidationByPcr(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    schema = models.CharField(max_length=999, blank=True, null=True)
    created_at_field = models.DateTimeField(db_column='created_at$', blank=True, null=True)
    creator_id_field = models.CharField(db_column='creator_id$', max_length=999, blank=True, null=True)
    entry_id_field = models.CharField(db_column='entry_id$', max_length=999, blank=True, null=True)
    archived_field = models.BooleanField(db_column='archived$', blank=True, null=True)
    archive_purpose_field = models.CharField(db_column='archive_purpose$', max_length=999, blank=True, null=True)
    custom_field = models.TextField(db_column='custom$', blank=True, null=True)
    validation_status_field = models.CharField(db_column='validation_status$', max_length=999, blank=True, null=True)
    validation_comment_field = models.CharField(db_column='validation_comment$', max_length=999, blank=True, null=True)
    field_validation_field = models.TextField(db_column='field_validation$', blank=True, null=True)
    entity = models.CharField(max_length=999, blank=True, null=True)
    batch = models.CharField(max_length=999, blank=True, null=True)
    gene = models.CharField(max_length=999, blank=True, null=True)
    primer1 = models.CharField(max_length=999, blank=True, null=True)
    primer2 = models.CharField(max_length=999, blank=True, null=True)
    size = models.CharField(max_length=999, blank=True, null=True)
    results = models.CharField(max_length=999, blank=True, null=True)
    comments = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'validation_by_pcr'


class WaterSolubleMetabolites(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    request_id_field = models.CharField(db_column='request_id$', max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'water_soluble_metabolites'


class Workflow(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    source_id = models.CharField(max_length=999, blank=True, null=True)
    alias = models.CharField(max_length=999, blank=True, null=True)
    name = models.CharField(max_length=999, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=999, blank=True, null=True)
    last_stage_completed = models.CharField(max_length=999, blank=True, null=True)
    last_stage_completed_at = models.DateTimeField(blank=True, null=True)
    workflow_template_version_id = models.CharField(max_length=999, blank=True, null=True)
    url = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'workflow'


class WorkflowTemplate(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    name = models.CharField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'workflow_template'


class WorkflowTemplateVersion(models.Model):
    id = models.CharField(max_length=999, blank=True, primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    workflow_template_id = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'workflow_template_version'
