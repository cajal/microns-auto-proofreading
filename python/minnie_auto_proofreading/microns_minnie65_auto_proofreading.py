import datajoint as dj

schema = dj.schema('microns_minnie65_auto_proofreading', create_tables=True)
schema.spawn_missing_classes()
