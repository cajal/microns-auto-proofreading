if __name__ == '__main__':
    import datajoint_plus
    print(f'Using datajoint_plus version: {datajoint_plus.__version__}')
    from microns_morphology.minnie_morphology import minnie65_morphology_v2 as m65mor2
    m65mor2.DecimatedMesh.Maker.populate(reserve_jobs=True, order='random', suppress_errors=True)

