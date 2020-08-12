import datashader.geo as dgeo
import hvplot.xarray
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr


def _hillshade_one_run(ds, time_dim, elev_var, **kwargs):
    elev = ds[elev_var]
    
    if time_dim is not None:
        # TODO: use shortcut=True
        # https://github.com/holoviz/datashader/issues/871
        hshade = elev.groupby(time_dim).apply(dgeo.hillshade, shortcut=False,
                                              **kwargs)
    else:
        hshade = dgeo.hillshade(elev, **kwargs)
    
    return hshade

    # TODO: related to todo above
    #return (hshade
    #        .rename(dim_0='y', dim_1='x')
    #        .assign_coords(x=ds.x, y=ds.y))


def hillshade(ds, time_dim='time', batch_dim=None,
              elev_var='topography__elevation', **kwargs):
    
    if batch_dim is not None:
        hda = []
        for _, bds in ds.groupby(batch_dim):
            hda.append(_hillshade_one_run(bds, time_dim, elev_var, **kwargs))
        return xr.concat(hda, batch_dim)
    
    else:
        return _hillshade_one_run(ds, time_dim, elev_var, **kwargs)
    
    
def plot_variable_shaded(ds, var, time_dim='time', batch_dim=None,
                         cmap=plt.cm.viridis, clim=None, log=False):

    if batch_dim is not None:
        groupby = [batch_dim, time_dim]
    else: 
        groupby = time_dim
        
    if log:
        values = np.log(ds[var])
    else:
        values = ds[var]

    image_plot = values.hvplot.image(
        x='x', y='y', cmap=cmap,
        groupby=groupby, data_aspect=1,
        frame_width=400, frame_height=400,
    )
    
    if clim is not None:
        image_plot = image_plot.opts(clim=clim)

    hillshade_plot = hillshade(ds, time_dim=time_dim, batch_dim=batch_dim).hvplot.image(
        x='x', y='y', cmap=plt.cm.gray, alpha=0.3,
        colorbar=False, hover=False, groupby=groupby
    )
    
    return image_plot * hillshade_plot