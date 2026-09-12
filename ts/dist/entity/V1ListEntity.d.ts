import { FreeMusicEntityBase } from '../FreeMusicEntityBase';
import type { FreeMusicSDK } from '../FreeMusicSDK';
import type { Control } from '../types';
import type { V1List, V1ListLoadMatch, V1ListListMatch } from '../FreeMusicTypes';
declare class V1ListEntity extends FreeMusicEntityBase<V1List> {
    constructor(client: FreeMusicSDK, entopts: any);
    make(this: V1ListEntity): V1ListEntity;
    load(this: any, reqmatch?: V1ListLoadMatch, ctrl?: Control): Promise<V1ListEntity>;
    list(this: any, reqmatch?: V1ListListMatch, ctrl?: Control): Promise<V1ListEntity[]>;
}
export { V1ListEntity };
