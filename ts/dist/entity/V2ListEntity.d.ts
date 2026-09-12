import { FreeMusicEntityBase } from '../FreeMusicEntityBase';
import type { FreeMusicSDK } from '../FreeMusicSDK';
import type { Control } from '../types';
import type { V2List, V2ListLoadMatch } from '../FreeMusicTypes';
declare class V2ListEntity extends FreeMusicEntityBase<V2List> {
    constructor(client: FreeMusicSDK, entopts: any);
    make(this: V2ListEntity): V2ListEntity;
    load(this: any, reqmatch?: V2ListLoadMatch, ctrl?: Control): Promise<V2ListEntity>;
}
export { V2ListEntity };
