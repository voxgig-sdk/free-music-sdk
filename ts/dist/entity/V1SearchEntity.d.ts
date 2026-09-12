import { FreeMusicEntityBase } from '../FreeMusicEntityBase';
import type { FreeMusicSDK } from '../FreeMusicSDK';
import type { Control } from '../types';
import type { V1Search, V1SearchLoadMatch, V1SearchListMatch } from '../FreeMusicTypes';
declare class V1SearchEntity extends FreeMusicEntityBase<V1Search> {
    constructor(client: FreeMusicSDK, entopts: any);
    make(this: V1SearchEntity): V1SearchEntity;
    load(this: any, reqmatch?: V1SearchLoadMatch, ctrl?: Control): Promise<V1SearchEntity>;
    list(this: any, reqmatch?: V1SearchListMatch, ctrl?: Control): Promise<V1SearchEntity[]>;
}
export { V1SearchEntity };
